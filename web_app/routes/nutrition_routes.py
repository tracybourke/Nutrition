#This is the "web_app/routes/nutrition_routes.py" file...

from flask import Blueprint, request, render_template

from app.edanam import fetch_nutrtion_data, format_pct

nutrition_routes = Blueprint("nutrition_routes", __name__)


@nutrition_routes.route("/nutrition/dashboard")
def nutrition_dashboard():
    print("NUTRITION DASHBOARD...")

    try:
        data = fetch_nutrition_data()
        latest = data[0]
        latest_rate_pct = format_pct(float(latest["value"]))
        latest_date = latest["date"]

        #flash("Fetched Latest Unemployment Data!", "success")
        return render_template("nutrition_dashboard.html",
            latest_rate_pct=latest_rate_pct,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Data Error. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

@nutrition_routes.route("/api/edanam.json")
def edanam_api():
    print("NUTRITION DATA (API)...")

    try:
        data = fetch_nutrition_data()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Data Error. Please try again."}, 404