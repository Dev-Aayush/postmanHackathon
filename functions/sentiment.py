from cgitb import text
from textblob import TextBlob


def sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity == 0:
        return "Neutral"
    elif polarity > 0:
        return "Positive"
    else:
        return "Negative"


def subjectivity(text):
    analysis = TextBlob(text)
    return int(analysis.sentiment.subjectivity*100)


# text = '''
# Tata Nexon recorded 14,315 unit sales in March 2022 as against 8,683 units during the same period last year with a YoY growth of 65 per cent Tata Motors finished third in the overall sales standings in March 2022 as 42,295 units were registered against 29,655 units during the corresponding period in 2021 with YoY volume growth of 43 per cent. In comparison to February 2022, the homegrown manufacturer posted an MoM growth of 6 per cent as 39,980 units were sold in that period. Tata had a total market share of 13.2 per cent and the Nexon was the most sold model within the brand’s portfolio and it was also the top volume gatherer in the SUV space. The compact SUV was first introduced back in late 2017 and it received a big upgrade in early 2020. It has played an integral role in Tata recording good sales tally every month. In March 2022, the Nexon recorded 14,315 unit sales as against 8,683 units during the same period last year with a healthy YoY surge of 65 per cent. With the highest YoY growth amongst the top ten models, the sub-four-metre SUV finished fourth overall. It beat popular SUVs like Maruti Suzuki Vitara Brezza and Hyundai Creta. The Nexon is currently retailed in two engine options: a 1.2-litre turbocharged three-cylinder petrol and a 1.5-litre four-cylinder diesel. The former delivers a maximum power output of 120 PS and 170 Nm of peak torque while the latter kicks out 110 PS and 260 Nm. Both are paired with a six-speed manual transmission as standard or a six-speed AMT as an option. The SUV is priced between Rs. 7.42 lakh and Rs. 13.74 lakh (ex-showroom) and it can be had in XE, XM, XT, XZ and XZ+ variants and recently the Kaziranga edition was introduced. Foliage Green, Flame Red, Pure Silver, Daytona Grey, Calgary White, and Atlas Black are the available colour options. It competes against Hyundai Venue, Kia Sonet, Nissan Magnite, Renault Kiger, Honda WR-V, etc. The equipment list of the Tata Nexon comprises a touchscreen infotainment system with Apple CarPlay and Android Auto compatibility, flat-bottom steering wheel with mounted controls, automatic climate control, push-button start/stop, sunroof, and so on. It has a Global NCAP safety rating of five stars.
# '''

# print(sentiment(text))
# print(subjectivity(text))
