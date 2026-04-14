from app import app
from models import db, Exercise, Workout, WorkoutExercises
from datetime import datetime

with app.app_context():
	Exercise.query.delete()
	Workout.query.delete()
	WorkoutExercises.query.delete()

	

	exercise1 = Exercise(name='Running', category='cardio', equipment=False)
	exercise2 = Exercise(name='Push-ups', category='strength', equipment=False)
	exercise3 = Exercise(name='Yoga', category='flexibility', equipment=False)
	exercise4 = Exercise(name='Plank', category='balance', equipment=False)
	db.session.add_all([exercise1, exercise2, exercise3, exercise4])


	workout1 = Workout(date= datetime(2023, 5, 18), duration_minutes=30, notes='Morning run in my estate')
	workout2 = Workout(date= datetime(2023, 5, 19), duration_minutes=20, notes='Muscles, here I come!')
	workout3 = Workout(date= datetime(2023, 5, 20), duration_minutes=45, notes='Namaste!')
	workout4 = Workout(date= datetime(2023, 5, 21), duration_minutes=15, notes='Abs day!')
	db.session.add_all([workout1, workout2, workout3, workout4])

	db.session.commit()
 

	we1 = WorkoutExercises(workout_id=workout1.id, exercise_id=exercise1.id, reps=10, sets=3, duration_seconds=2400)
	we2 = WorkoutExercises(workout_id=workout2.id, exercise_id=exercise2.id, reps=15, sets=4, duration_seconds=1200)

	db.session.add_all([we1, we2])
	db.session.commit()
	print("Database seeded successfully!")