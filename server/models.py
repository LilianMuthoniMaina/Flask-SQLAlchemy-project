from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates, relationship
from sqlalchemy import MetaData


metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})


db = SQLAlchemy(metadata=metadata)

# Define Models here
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    equipment = db.Column(db.Boolean)

    workout_exercises = db.relationship('WorkoutExercises', back_populates='exercise', cascade='all, delete-orphan')
    workouts = db.relationship('Workout', secondary='workout_exercises', back_populates='exercises', overlaps="workout_exercises")
    

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        return name

    



class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship('WorkoutExercises', back_populates='workout', cascade='all, delete-orphan')
    exercises = db.relationship('Exercise', secondary='workout_exercises', back_populates='workouts', overlaps="workout_exercises")
    
    @validates('duration_minutes')
    def validate_duration(self, key, duration):
        if duration and duration <= 0:
            raise ValueError("Workout duration must be greater than 0 minutes.")
        return duration




class WorkoutExercises(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.ForeignKey('exercises.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship('Workout', back_populates='workout_exercises', overlaps="exercises,workouts")
    exercise = db.relationship('Exercise', back_populates='workout_exercises', overlaps="exercises,workouts")

    
