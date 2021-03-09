#!/bin/bash
export FLASK_APP=recipes.main
export DATABASE_URL="postgresql://postgres:tslzXGUXh1iY1WlxbxBO@recipe-db-instance.cmzxnjhlalty.us-east-2.rds.amazonaws.com:5432/postgres"
export SQLALCHEMY_TRACK_MODIFICATIONS=False
export ENV=production
export FLASK_ENV=production