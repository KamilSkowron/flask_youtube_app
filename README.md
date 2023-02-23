# flask_youtube_app

# What is it?
http://localhost:5000/home - Private youtube page with our favourite movies. We can adds,
![image](https://user-images.githubusercontent.com/86384863/220916165-e5d68a17-20cb-4cab-842e-5391ead2ce7e.png)

http://localhost:5000/upload - Upload movies to private page
![image](https://user-images.githubusercontent.com/86384863/220915691-87bd83f8-042f-4590-8206-7eb71ef80f21.png)

http://localhost:5000/ - RESTful API in Swagger
![image](https://user-images.githubusercontent.com/86384863/220916334-224bcda2-fe53-4f39-bb0c-d219df4d24cc.png)

http://localhost:5000/explore - Actual Youtube trends with search threw countries and categories
![image](https://user-images.githubusercontent.com/86384863/220916700-1d36af5a-e01a-47cd-a522-ab13d7551de3.png)


# How to run?
There is two ways to checkout this project:
1) Clone all repo
- pip install -r requirements.txt
- python run.py

2) Download Dockerfile
- docker build -t yt_app .
- docker run -p5000:5000 --name yt_app yt_app
