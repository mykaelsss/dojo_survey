from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def get_last_dojo(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_db').query_db(query)
        return Dojo(results[0])


    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos(name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s, %(comment)s)"
        return connectToMySQL('dojo_survey_db').query_db(query,data)


    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 charaters long.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("Please select a location.")
        if len(dojo['language']) < 1:
                is_valid = False
                flash("Please select a language.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Please Enter a comment that is at least 3 characters long.")
        return is_valid
