from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource
from models import db, Exercise, Workout, WorkoutExercises
from flask_migrate import Migrate
from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    category = fields.Str()
    equipment = fields.Bool()

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(validate=validate.Range(min=1))
    notes = fields.Str()

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

class Workouts(Resource):
    def get(self):
        workouts = Workout.query.all()
        return make_response(jsonify(workouts_schema.dump(workouts)), 200)

    def post(self):
        json_data = request.get_json()
        try:
            data = workout_schema.load(json_data)
            new_workout = Workout(**data)
            db.session.add(new_workout)
            db.session.commit()
            return workout_schema.dump(new_workout), 201
        except ValidationError as err:
            return err.messages, 400

class WorkoutById(Resource):
    def get(self, id):
        workout = Workout.query.get_or_404(id)
        return workout_schema.dump(workout), 200
        
    def delete(self, id):
        workout = Workout.query.get_or_404(id)
        db.session.delete(workout)
        db.session.commit()
        return '', 204

api.add_resource(Workouts, '/workouts')
api.add_resource(WorkoutById, '/workouts/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)




