import tensorflow as tf

#check the version of tf
if not tf.__version__ == '2.16.1':
    print(tf.__version__)
    raise ValueError("Please upgrade to new....")