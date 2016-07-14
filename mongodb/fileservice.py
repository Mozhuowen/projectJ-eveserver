#!coding=utf-8
from util import str_util


def save_upload_file(request):
    print request.headers
    try:
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = str_util.get_random_string(16) + '.' + get_file_type(file.filename)
                print filename
                file.save('/usr/local/python/jjimages/', filename)
                return {
                    'filename': filename
                }, 1, ''
    except Exception, e:
        print Exception, e
        return {}, 0, '上传文件失败'


def allowed_file(filename):
    return True


def get_file_type(filename):
    if not filename.__contains__('.'):
        return 'jpg'
    else:
        type = filename.split('.')[-1]
        return type
