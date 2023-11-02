from flask import Flask, request, jsonify
from graphene import ObjectType, Schema
from app.api.schema import schema  # Import your GraphQL schema

app = Flask(__name__)

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    result = schema.execute(data.get('query'))
    return jsonify(result.data)

if __name__ == '__main__':
    app.run()
