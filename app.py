from flask import Flask, render_template, url_for, redirect
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta


app = Flask(__name__)

scheduler = BackgroundScheduler()

ren = []
lt = []
with open('text.txt', 'r', encoding='utf-8') as f:
    r = f.readlines()
    for line in r:
        if len(line) < 5:
            pass
        else:
            lt.append(line)

@app.route('/')
def jobb():
    if "2023-05-31" == datetime.now().strftime("%Y-%m-%d"):
        renn = lt
        lenght = len(renn) - 1
        rr = renn[lenght]
        _t = rr.find(' –')
        rrr = []
        rrr.append(rr[1:_t - 1])
        rrr.append(rr[_t + 3:len(rr) - 1])

        return render_template('index.html', items=lt, item=rrr)

    elif "2023-05-10" == datetime.now().strftime("%Y-%m-%d"):
        rr = lt[9]
        _t = rr.find(' –')
        rrr = []
        rrr.append(rr[1:_t - 1])
        rrr.append(rr[_t + 3:len(rr) - 1])

        return render_template('index.html', item=rrr)


    elif len(ren) > 0:
        lenght = len(ren) - 1
        rr = ren[lenght]
        _t = rr.find(' –')
        rrr = []
        rrr.append(rr[1:_t-1])
        rrr.append(rr[_t + 3:len(rr) - 1])

        return render_template('index.html', item=rrr)

    else:
        return render_template('index.html', item='')

def job(item):
    res = 'Scheduled job executed' + item + str(datetime.now())
    ren.append(item)
    scheduler.remove_job(item)

count = datetime(2023, 5, 1)
for item in lt:
    scheduler.add_job(job, 'date', run_date=count, args=[item], id=item)
    count = count + timedelta(days=1)

# scheduler.add_job(job, 'cron', hour=7, minute=27)
scheduler.print_jobs()
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)