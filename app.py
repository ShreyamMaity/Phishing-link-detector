from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/", methods=["POST"])
def my_form_post():
    url = request.form["url"]
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(firefox_options=opts)
    _take = url
    removable1 = "https://"
    removable2 = "http://"

    if removable1 in _take:
        _take = _take.replace('https://', '')
    elif removable2 in _take:
        _take = _take.replace('http://', '')
    else:
        _take = _take

    browser.get("https://" + _take)


    time.sleep(3)
    # print(browser.current_url)
    _toMatch = browser.current_url
    time.sleep(1)
    browser.quit()

    # Python program for KMP Algorithm
    def KMPSearch(pat, txt):
        M = len(pat)
        N = len(txt)


        lps = [0] * M
        j = 0  # index for pat[]

        computeLPSArray(pat, M, lps)

        i = 0  # index for txt[]
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                #Return value to use it
                return 100
                j = lps[j - 1]

            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:

                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

    def computeLPSArray(pat, M, lps):
        len = 0

        lps[0]  # lps[0] is always 0
        i = 1


        while i < M:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:


                if len != 0:
                    len = lps[len - 1]


                else:
                    lps[i] = 0
                    i += 1

    txt = str(_toMatch)
    pat = "ngrok.io"

    #KMPSearch(pat, txt)


    if KMPSearch(pat, txt) == 100 :
        status = "Phishing Link"
    else :
        status = "Safe Link"

    urlInfo = _take

    return render_template("form.html",
                           urlUpdate=urlInfo,
                           stausUpdate=status)

if __name__ == "__main__":
    app.run(debug=True)
