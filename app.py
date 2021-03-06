from flask import Flask, jsonify, request
import json
import datetime as dt
import get_changes
from format_csv import gen_changed_data
from multiprocessing import Process
# from threading import ThreadError


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False  # ソートをそのまま
json_open = open('data.json', 'r')
json_load = json.load(json_open)


def date_to_weekday(dates):
    year = int(dates[:4])
    month = int(dates[4:6])
    day = int(dates[6:])
    weekday = dt.date(year, month, day).strftime('%a')
    return weekday


@app.route('/', methods=['GET'])
def index():
    return "苫小牧高専授業変更情報API"


@app.route('/api/v1/classes/<grade>/<course>/<dates>', methods=['GET'])
def foo(grade, course, dates):
    date_list, grade_list, course_list, time_period_list, subjects_after_change, data_length, line_count = gen_changed_data(
    )
    grade = str(grade)
    course = str(course)
    dates = str(dates)
    # flag = {"a": type(grade), "b": type(course), "c": type(dates)}
    # change = data_length
    # returnval = []
    dayOfWeek = date_to_weekday(dates)
    if request.method == 'GET':
        if dayOfWeek == "Mon":
            data = {
                "1": {
                    "time": 1,
                    "subject": "応用物理i"
                },
                "2": {
                    "time": 2,
                    "subject": "応用物理i"
                },
                "3": {
                    "time": 3,
                    "subject": "ソフトウェア工学"
                },
                "4": {
                    "time": 4,
                    "subject": "ソフトウェア工学"
                },
                "5": {
                    "time": 5,
                    "subject": "ソフトウェアデザイン演習ii"
                },
                "6": {
                    "time": 6,
                    "subject": "ソフトウェアデザイン演習ii"
                },
                "7": {
                    "time": 7,
                    "subject": ""
                },
                "8": {
                    "time": 8,
                    "subject": ""
                }
            }

        elif dayOfWeek == "Tue":
            data = {
                "1": {
                    "time": 1,
                    "subject": "専門選択"
                },
                "2": {
                    "time": 2,
                    "subject": "専門選択"
                },
                "3": {
                    "time": 3,
                    "subject": "一般選択"
                },
                "4": {
                    "time": 4,
                    "subject": "一般選択"
                },
                "5": {
                    "time": 5,
                    "subject": "ビジネスi"
                },
                "6": {
                    "time": 6,
                    "subject": "ビジネスi"
                },
                "7": {
                    "time": 7,
                    "subject": ""
                },
                "8": {
                    "time": 8,
                    "subject": ""
                }
            }

        elif dayOfWeek == "Wed":
            data = {
                "1": {
                    "time": 1,
                    "subject": "英語ivC"
                },
                "2": {
                    "time": 2,
                    "subject": "英語ivC"
                },
                "3": {
                    "time": 3,
                    "subject": "ハードウェア総論"
                },
                "4": {
                    "time": 4,
                    "subject": "ハードウェア総論"
                },
                "5": {
                    "time": 5,
                    "subject": "応用数学i"
                },
                "6": {
                    "time": 6,
                    "subject": "応用数学i"
                },
                "7": {
                    "time": 7,
                    "subject": "HR"
                },
                "8": {
                    "time": 8,
                    "subject": ""
                }
            }

        elif dayOfWeek == "Thu":
            data = {
                "1": {
                    "time": 1,
                    "subject": "回路理論ii"
                },
                "2": {
                    "time": 2,
                    "subject": "回路理論ii"
                },
                "3": {
                    "time": 3,
                    "subject": ""
                },
                "4": {
                    "time": 4,
                    "subject": ""
                },
                "5": {
                    "time": 5,
                    "subject": "情報科学・工学実験iii"
                },
                "6": {
                    "time": 6,
                    "subject": "情報科学・工学実験iii"
                },
                "7": {
                    "time": 7,
                    "subject": "情報科学・工学実験iii"
                },
                "8": {
                    "time": 8,
                    "subject": ""
                }
            }
        elif dayOfWeek == "Fri":
            data = {
                "1": {
                    "time": 1,
                    "subject": "データベース"
                },
                "2": {
                    "time": 2,
                    "subject": "データベース"
                },
                "3": {
                    "time": 3,
                    "subject": "情報数学"
                },
                "4": {
                    "time": 4,
                    "subject": "情報数学"
                },
                "5": {
                    "time": 5,
                    "subject": ""
                },
                "6": {
                    "time": 6,
                    "subject": ""
                },
                "7": {
                    "time": 7,
                    "subject": ""
                },
                "8": {
                    "time": 8,
                    "subject": ""
                }
            }
        # if dayOfWeek == "Sat":
        #     data = [{"今日は": "土曜日です"}]
        # if dayOfWeek == "Sun":
        #     data = [{"今日は": "日曜日です"}]
        else:
            data = {"holiday": "Today is a holiday!!!", "dayOfWeek": dayOfWeek}
        # j = json.loads(data)

        if dates in date_list:
            # index = format_csv.time_period_list[0]
            # flag = int(format_csv.line_count)
            # ['subject']
            # returnval.append({'len': data_length})
            for row in range(data_length):

                # returnval.append({
                #     # 'row': row,
                #     "time": time_period_list[row],
                #     'date': date_list[row]
                # })
                if dates == date_list[row] and course == course_list[
                        row] and grade == grade_list[row]:
                    data[time_period_list[row]][
                        "subject"] = subjects_after_change[row]
                    # change = 1
                    # flag = 1
            # print(format_csv.grade[row])
            # data[str(
            #     format_csv.time_period_list
            # )]['subject'] = format_csv.subjects_after_change[row]
        # data[times][subject] = new_data
        result = {
            'status': 'OK',
            'data': data,
            'csv_line': int(line_count),
            # 'changed': change,
            # 'return': returnval
        }
    return jsonify(result), 200


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('/favicon.ico')
    # send_from_directory(
    #     os.path.join(app.root_path, 'static/img'),
    #     'favicon.ico',
    # )


# @app.errorhandler(400)
# @app.errorhandler(404)
# def error_handler(error):
#     return jsonify
#     ({
#         'error': {
#             'code': error.description['code'],
#             'message': error.description['message']
#         }
#     }), error.code

if __name__ == "__main__":
    # scheduler = AsyncIOScheduler()
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(fuga, trigger='interval', seconds=10)
    # scheduler.start()
    # asyncio.get_event_loop().run_forever()
    p = Process(target=get_changes.main)
    p.start()
    app.debug = False # debugをTrueにするとmainが2度動いてしまう
    app.run(host='0.0.0.0', port=5000)
    # , threaded=True)
    # , use_reloader=False, threaded=False) True
