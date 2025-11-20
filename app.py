import os

import logging

import json

import time

from flask import Flask, jsonify, request



# SRE PRINCIPLE 1: Configuration via Environment Variables

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")



# SRE PRINCIPLE 2: Structured Logging (JSON)

class JsonFormatter(logging.Formatter):

    def format(self, record):

        log_record = {

            "timestamp": self.formatTime(record),

            "level": record.levelname,

            "message": record.getMessage(),

            "module": record.module,

            "path": request.path if request else "system",

            "method": request.method if request else "system",

            "version": APP_VERSION

        }

        return json.dumps(log_record)



# Setup Logging

handler = logging.StreamHandler()

handler.setFormatter(JsonFormatter())

logger = logging.getLogger()

logger.setLevel(LOG_LEVEL)

logger.addHandler(handler)



app = Flask(__name__)



@app.route('/')

def home():

    logger.info("Home endpoint accessed")

    return jsonify({

        "message": "Resilient API is running",

        "version": APP_VERSION,

        "status": "stable",

        "environment": os.getenv("FLASK_ENV", "production")

    })



# SRE PRINCIPLE 3: Health Checks / Liveness Probes

@app.route('/health')

def health():

    return jsonify({"status": "healthy"}), 200



if __name__ == '__main__':

    logger.info(f"Starting Resilient API Application v{APP_VERSION}...")

    app.run(host='0.0.0.0', port=5000)

