from os import system

system(f"python -m pip install --upgrade pip")
system(f"pip install --upgrade wheel cmake setuptools")
system(f"pip install --upgrade numpy pandas matplotlib seaborn xlrd joblib plotly scikit-learn lightgbm xgboost "
       f"catboost")
system(f"pip install --upgrade imutils flask flask_Cors")
system(f"pip install --upgrade opencv_python PyInstaller boto3 fast_enum pytesseract json2table beautifulsoup4")
system(f"pip install --upgrade google-cloud google-cloud-vision google-cloud-storage google-api-core")
system(f"pip install --upgrade lxml pipreqs vulture")
system(f"pip install --upgrade datapackage wordcloud pydotplus unidecode pgeocode geotext")
system(f"pip install --upgrade tensorflow")
system(f"pip install --upgrade spacy")
system(f"python -m spacy download en_core_web_md")
system(f"pip install --upgrade gensim")
system(f"pip install --upgrade pandas-profiling")
system(f"pip install --upgrade passporteye")
system(f"pip install --upgrade face_recognition")
system(f"pip install --upgrade imblearn ply pyspellchecker")
system(f"python update_from_freeze_file.py")
# system(f"pip install --upgrade pdf2image pyPDF4 pdfkit")

