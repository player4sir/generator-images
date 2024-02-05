from flask import Flask, request, jsonify
import os
from re_edge_gpt import ImageGen

app = Flask(__name__)

auth_cookie = os.environ.get('AUTH_COOKIE')
sync_gen = ImageGen(auth_cookie=auth_cookie)

@app.route('/g', methods=['GET'])
def generate_image():
    try:
        prompt = request.args.get('prompt')

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        image_list = sync_gen.get_images(prompt=prompt)
        return jsonify({"images": image_list})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
