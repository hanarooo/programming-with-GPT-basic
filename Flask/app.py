from flask import Flask, render_template, request
import random
import requests
app = Flask(__name__)

@app.route('/')
def home():
    name = '하나루'
    lotto = [16, 18, 22, 43, 32, 11]
    
    
    

    def generate_lotto_numbers():
        lotto_numbers = random.sample(range(1, 46), 6)
        lotto_numbers.sort()
        return lotto_numbers

    recommended_numbers = generate_lotto_numbers()
    print("로또 추천 번호:", recommended_numbers)



    def count_common_elements(lotto, recommended_numbers):
        commen_elements = set(lotto) & set(recommended_numbers)
        return len(commen_elements)

    common_count = count_common_elements(lotto, recommended_numbers)
    print("같은 요소의 개수: ", common_count)

    

    context = {
        "name" : name,
        "lotto" : lotto,
        "recommended_numbers" : recommended_numbers,
        "common_count" : common_count,
    }

    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():
    return 'This is Mypage!'

@app.route('/movie')
def movie():
    query = request.args.get('query')
    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}"
    )
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    return render_template('movie.html', data=movie_list)

@app.route('/answer')
def answer():
    if request.args.get('query'): query = request.args.get('query')
    else: query='20230601'
    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={query}"
    )
    rjson = res.json()
    movie_list = rjson["boxOfficeResult"]["weeklyBoxOfficeList"]
    return render_template('answer.html', data=movie_list)



if __name__ == '__main__':  
    app.run(debug=True)