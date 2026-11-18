def calculate_risk(
    rainfall,
    temperature,
    population
):

    score = (
        rainfall*0.3
        + temperature*2
        + population*0.4
    )

    return round(score,2)
