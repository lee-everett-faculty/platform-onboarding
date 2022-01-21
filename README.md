# Platform Onboarding

## Instructions

1. Create a new Platform project on the [Projects page](https://datascience.my.faculty.ai/home).

1. Download the [data file](https://github.com/Kaushik-Varma/linear_regression_model_python/raw/main/Company_data.csv)
   to your computer. Then go to _Datasets_ (left menu) and upload the file there. There should be
   a file called `Company_data.csv` in the file tree on the left now.

1. Go to the _Environments_ page (left menu) and create a new environment called `latest mlflow`. 
   In the _PYTHON_ section, add the `mlflow` package of a `pip` type. Use `==` `1.20.2` as the
   version constraint.
   
1. Switch to the _Workspace_ page (left menu) and click the _+_ button to create a new server.
   In the _Environments_ dropdown, select `latest mlflow`. Leave other inputs as default
   (_Jupyter Server_, _1 core, 4 GB_) and click _CREATE SERVER_.

1. Open a new terminal on your server and run following:

   1. Close the code repository: `git clone https://github.com/tomas-milata/platform-onboarding.git` 
   1. Navigate to the right directory: `cd platform-onboarding`.
   1. Run the code to train your model: `python train.py`.



apply environment to the server

git clone

run training code

go to experiments

register model

go to apps

create app

change app code to use the model

start app

# Credits

- [Linear regression chart using Altair]( https://altair-viz.github.io/user_guide/transform/regression.html). This demo
  uses a modified example from this article.
- [Data](https://github.com/Kaushik-Varma/linear_regression_model_python/blob/main/Company_data.csv)
