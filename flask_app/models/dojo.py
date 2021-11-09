# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the user table from our database
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def submit_survey(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at ) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW() );"
        return connectToMySQL('survey_schema').query_db(query,data)

    @classmethod
    def get_survey(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('survey_schema').query_db(query,data)
        if len(results) == 0:
            return False
        return Dojo(results[0])

    staticmethod
    def validate_survey(dojo):
        is_valid = True #we assume this is true
        if len(dojo['name']) <3:
            flash ("Name must be at least 3 characters")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash ("You must provide a valid comment")
            is_valid = False
        return is_valid