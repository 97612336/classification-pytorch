import traceback

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from classification import Classification

app = Flask(__name__)
api = Api(app)

classfication = Classification()


class ImgClass(Resource):
    def get(self):
        # 从查询字符串中获取图片路径参数
        img_path = request.args.get('img_path')

        if not img_path:
            return {
                "code": 1,
                "msg": "no img path",
                "res": False,
                "pro_num": 0
            }

        # 开始进行图片检测
        try:
            res, pro_num = classfication.flask_detect_image(img_path)
        except Exception as e:
            print(traceback.format_exc())
            return {
                "code": 2,
                "msg": str(e),
                "res": False,
                "pro_num": 0
            }

        return {
            "code": 0,
            "msg": "success",
            "res": res,
            "pro_num": str(pro_num)
        }


# 添加资源和路由
api.add_resource(ImgClass, '/img_class')

if __name__ == '__main__':
    app.run(debug=True)
