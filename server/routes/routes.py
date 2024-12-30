# routes.py

# Authentication routes
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if User.query.filter_by(aadhar_number=data['aadhar_number']).first():
        return jsonify({'message': 'Aadhar number already registered'}), 400
    
    user = User(
        name=data['name'],
        aadhar_number=data['aadhar_number'],
        is_admin=data.get('is_admin', False)
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(aadhar_number=data['aadhar_number']).first()
    
    if user and user.check_password(data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, Config.SECRET_KEY)
        
        return jsonify({
            'token': token,
            'is_admin': user.is_admin
        })
    
    return jsonify({'message': 'Invalid credentials'}), 401

# Voting routes
@app.route('/electors', methods=['GET'])
@token_required
def get_electors(current_user):
    candidates = Candidate.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'position': c.position,
        'votes': c.votes
    } for c in candidates])

@app.route('/vote/<int:elector_id>', methods=['POST'])
@token_required
def vote(current_user, elector_id):
    if current_user.has_voted:
        return jsonify({'message': 'You have already voted'}), 400
    
    candidate = Candidate.query.get_or_404(elector_id)
    
    vote = Vote(user_id=current_user.id, candidate_id=elector_id)
    candidate.votes += 1
    current_user.has_voted = True
    
    db.session.add(vote)
    db.session.commit()
    
    return jsonify({'message': 'Vote recorded successfully'})

@app.route('/vote/counts', methods=['GET'])
def get_vote_counts():
    candidates = Candidate.query.order_by(Candidate.votes.desc()).all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'position': c.position,
        'votes': c.votes
    } for c in candidates])

# User profile routes
@app.route('/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    return jsonify({
        'id': current_user.id,
        'name': current_user.name,
        'aadhar_number': current_user.aadhar_number,
        'is_admin': current_user.is_admin,
        'has_voted': current_user.has_voted
    })

@app.route('/profile/password', methods=['PUT'])
@token_required
def change_password(current_user):
    data = request.json
    if not current_user.check_password(data['old_password']):
        return jsonify({'message': 'Invalid old password'}), 400
    
    current_user.set_password(data['new_password'])
    db.session.commit()
    
    return jsonify({'message': 'Password updated successfully'})

# Admin routes
@app.route('/electors', methods=['POST'])
@admin_required
def create_elector(current_user):
    data = request.json
    candidate = Candidate(
        name=data['name'],
        party=data['position']
    )
    
    db.session.add(candidate)
    db.session.commit()
    
    return jsonify({'message': 'Candidate created successfully'}), 201

@app.route('/electors/<int:elector_id>', methods=['PUT'])
@admin_required
def update_elector(current_user, elector_id):
    candidate = Candidate.query.get_or_404(elector_id)
    data = request.json
    
    candidate.name = data.get('name', candidate.name)
    candidate.position = data.get('position', candidate.position)
    
    db.session.commit()
    
    return jsonify({'message': 'Candidate updated successfully'})

@app.route('/electors/<int:elector_id>', methods=['DELETE'])
@admin_required
def delete_elector(current_user, elector_id):
    candidate = Candidate.query.get_or_404(elector_id)
    
    db.session.delete(candidate)
    db.session.commit()
    
    return jsonify({'message': 'Candidate deleted successfully'})

# API routes for testing
@app.route('/api/voters', methods=['GET'])
@admin_required
def get_voters(current_user):
    voters = User.query.filter_by(is_admin=False).all()
    return jsonify([{
        'id': v.id,
        'name': v.name,
        'aadhar_number': v.aadhar_number,
        'has_voted': v.has_voted
    } for v in voters])

@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'position': c.position,
        'votes': c.votes
    } for c in candidates])

@app.route('/api/voter/register', methods=['POST'])
@admin_required
def register_voter():
    data = request.json
    aadhar = generate_aadhar()
    temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    new_voter = User(
        name=data['name'],
        city=data['city'],
        contact=data['contact'],
        aadhar_number=aadhar,
        password=generate_password_hash(temp_password),
        is_admin=False
    )
    
    try:
        db.session.add(new_voter)
        db.session.commit()
        return jsonify({
            'message': 'Voter registered successfully',
            'aadhar_number': aadhar,
            'temporary_password': temp_password
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Registration failed'}), 400

@app.route('/api/candidate/register', methods=['POST'])
@admin_required
def register_candidate():
    data = request.json
    aadhar = generate_aadhar()
    
    new_candidate = Candidate(
        name=data['name'],
        age=data['age'],
        city=data['city'],
        contact=data['contact'],
        position=data['position'],
        nationality=data['nationality'],
        policy=data['policy'],
        aadhar_number=aadhar
    )
    
    try:
        db.session.add(new_candidate)
        db.session.commit()
        return jsonify({
            'message': 'Candidate registered successfully',
            'aadhar_number': aadhar
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Registration failed'}), 400
    
    

