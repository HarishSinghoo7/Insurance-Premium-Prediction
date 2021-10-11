import pandas as pd

from src import app
from flask import render_template, request, jsonify
from src.controller.prediction_controller import PredictionController
from src.controller.training_controller import TrainingController
from src.controller.db_migration_controller import DBMigrationController

# web routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        pred_controller = PredictionController()
        if 'file' in request.files:
            resp = pred_controller.bulk_data_prediction(request.files)
        else:
            resp = pred_controller.single_data_prediction(request.form)
        return render_template('home.html', predictions=resp)


@app.route('/training', methods=['GET'])
def training():
    tc = TrainingController()
    return tc.start_training()


@app.route('/db-migration', methods=['GET'])
def db_migration():
    try:
        DBMigrationController().migrate()
        return "Migration Complete!"
    except Exception as ex:
        return str(ex)
