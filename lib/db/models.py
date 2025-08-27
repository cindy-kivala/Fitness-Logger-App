
#SQLALCHEMY ATTEMPT
from sqlalchemy import Column, Integer, String, text, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base #relationship
from sqlalchemy.orm import relationship, Session

Base = declarative_base()

#User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    weight = Column(Float)

    # Relationship to WorkoutSession
    workout_sessions = relationship("WorkoutSession", back_populates="user")

    def __str__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age}, weight={self.weight})>"
    
    @classmethod
    def create(cls, session:Session, name, age, weight):
        """Convenience method to create and add a User to the DB."""
        user = cls(
            name=name, 
            age=age, 
            weight=weight
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    @classmethod
    def all(cls, session: Session):
        return session.query(cls).all()
    
    #update method
    def update_user(session, user_id, name=None, age=None, weight=None):
        user = session.query(User).get(user_id)
        if user:
           if name: user.name = name
           if age: user.age = age
           if weight: user.weight = weight
           session.commit()
           print(f"User {user_id} updated!")

    #delete method
    def delete_user(session, user_id):
        user = session.query(User).get(user_id)
        if user:
           session.delete(user)
           session.commit()
           print(f"User {user_id} deleted!")

    
#Exercise model
class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    muscle_group = Column(String)
    equipment = Column(String)
    description = Column(String)

    # Relationship to WorkoutSession through association table
    workout_sessions = relationship("WorkoutSessionExercise", back_populates="exercise")

    def __str__(self):
        return f"<Exercise(id={self.id}, name='{self.name}')>"
    
    @classmethod
    def create(cls, session:Session, name, muscle_group=None, equipment=None,  description=None):
        exercise = cls(
            name=name, 
            muscle_group=muscle_group, 
            equipment=equipment,
            description=description, 
        )
        session.add(exercise)
        session.commit()
        session.refresh(exercise)
        return exercise

    @classmethod
    def all(cls, session: Session):
        return session.query(cls).all()
    
    #update method
    def update_exercise(session, exercise_id, name=None, muscle_group=None, equipment=None, description=None):
        ex = session.query(Exercise).get(exercise_id)
        if ex:
           if name: ex.name = name
           if muscle_group: ex.muscle_group = muscle_group
           if equipment: ex.equipment = equipment
           if description: ex.description = description
           session.commit()
           print(f"Exercise {exercise_id} updated!")

    #delete method BE CAREFUL WITH THIS
    def delete_exercise(session, exercise_id):
        ex = session.query(Exercise).get(exercise_id)
        if ex:
           session.delete(ex)
           session.commit()
           print(f"Exercise {exercise_id} deleted!")


#WorkoutSession Model
class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    duration = Column(Integer)  # duration in minutes
    activity = Column(String)
    calories = Column(Integer)

    # Relationship back to User
    user = relationship("User", back_populates="workout_sessions")

    # Relationship to exercises via association table
    exercises = relationship(
        "WorkoutSessionExercise", 
        back_populates="workout_session",
        cascade= "all, delete-orphan" #cascade delete ensure that deleting a workout session also deletes its related WorkoutSessionExercise entries.
    )

    def __str__(self):
        return f"<WorkoutSession(id={self.id}, user_id={self.user_id}, date={self.date})>"
    
    @classmethod
    def create(cls, session:Session, user_id, activity, duration,calories, date=None):
        workout_session = cls(
            duration=duration, 
            activity=activity, 
            calories=calories, 
            user_id=user_id,
            date=date
        )

        session.add(workout_session)
        session.commit()
        session.refresh(workout_session)
        return workout_session
    
    @classmethod
    def find_by_id(cls, session: Session, session_id):
        return session.query(cls).filter_by(id=session_id).first()

    @classmethod
    def all(cls, session: Session):
        return session.query(cls).all()
    
    #update method
    def update_workout(session, session_id, activity=None, duration=None, calories=None, date=None):
        ws = session.query(WorkoutSession).get(session_id)
        if ws:
           if activity: ws.activity = activity
           if duration: ws.duration = duration
           if calories: ws.calories = calories
           if date: ws.date = date
           session.commit()
           print(f"Workout session {session_id} updated!")

    #delete method
    def delete_workout(session, session_id):
        ws = session.query(WorkoutSession).get(session_id)
        if ws:
           session.delete(ws)
           session.commit()
           print(f"Workout session {session_id} deleted!")


#ASSOCIATION TABLE
class WorkoutSessionExercise(Base): #backlinking our relaionship
    __tablename__ = "workout_session_exercises"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("workout_sessions.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)

    # Relationships back to WorkoutSession and Exercise
    workout_session = relationship("WorkoutSession", back_populates="exercises")
    exercise = relationship("Exercise", back_populates="workout_sessions")

    def __str__(self):
        return f"<WorkoutSessionExercise(id={self.id}, session_id={self.session_id}, exercise_id={self.exercise_id}, sets={self.sets}, reps={self.reps}, weight={self.weight})>"

    @classmethod
    def add_to_session(cls, session:Session, workout_session_id, exercise_id, sets, reps, weight):
        wse = cls(
            session_id=workout_session_id, 
            exercise_id=exercise_id, 
            sets=sets, 
            reps=reps, 
            weight=weight
        )
        session.add(wse)
        session.commit()
        session.refresh(wse)
        return wse
    
    def update_session_exercise(session, wse_id, sets=None, reps=None, weight=None):
        wse = session.query(WorkoutSessionExercise).get(wse_id)
        if wse:
           if sets: wse.sets = sets
           if reps: wse.reps = reps
           if weight: wse.weight = weight
           session.commit()
           print(f"Session exercise {wse_id} updated!")

    def delete_session_exercise(session, wse_id):
        wse = session.query(WorkoutSessionExercise).get(wse_id)
        if wse:
           session.delete(wse)
           session.commit()
           print(f"Session exercise {wse_id} removed from workout!")

