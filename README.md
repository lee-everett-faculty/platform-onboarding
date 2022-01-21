# Platform Onboarding

## Instructions

### Project

Create a new Platform project on the [Projects page](https://datascience.my.faculty.ai/home).

### Data Upload

1. Download the [data file](https://github.com/Kaushik-Varma/linear_regression_model_python/raw/main/Company_data.csv)
   to your computer. 
1. Then go to _Datasets_ (left menu) and upload the file there. There should be
   a file called `Company_data.csv` in the file tree on the left now.

### Setting Up / Customising Servers

1. Go to the _Environments_ page (left menu) and create a new environment called `latest mlflow`. 

1. In the _PYTHON_ section, add the `mlflow` package of a `pip` type. Use `==` `1.20.2` as the
   version constraint.
   
1. Switch to the _Workspace_ page (left menu) and click the _+_ button to create a new server.
   In the _Environments_ dropdown, select `latest mlflow`. Leave other inputs as default
   (_Jupyter Server_, _1 core, 4 GB_) and click _CREATE SERVER_.

### Training a Model

1. Open a new terminal on your server and run following:

   1. Close the code repository: `git clone https://github.com/tomas-milata/platform-onboarding.git` 
   1. Navigate to the right directory: `cd platform-onboarding`.
   1. Run the code to train your model: `python train.py`.

1. Go to the _Experiments_ (left menu). From the experiments list, select `ads`.
   Then should be 1 run in the `ads` experiment. Open that run.
   In the file tree under _ARTIFACTS_, click `linear_regression_model`.
   Click _REGISTER MODEL_ on the right and then create a new model (choose any name).
   Creating the model should navigate you to the _Models_ page.

### Making Predictions
   
1. In the page that shows details of your model, click _VIEW CODE SNIPPET_ and then
   copy the code to your clipboard.
   
1. Navigate back to the _Workspace_ page and open the `/project/platform-onboarding/app-predict/app.py`
   file in the editor.
   Paste the code snippet you copied into the file (under the `CHANGE ME` line) to make 
   it look something like:
   
   ```python
   model = faculty_models.load_mlmodel(
         project_id="YOUR PROJECT ID",
         model_id="YOUR MODEL ID"
   )
   ```

### App

1. Navigate to _Deployments_ > _Apps_ from the left menu. Create a new app
   of the `Plotly Dash` type with any name and domain name.
   Use the following app settings:
   
   - _WORKING DIRECTORY_: `/project/platform-onboarding/app-predict`
   - _PYTHON MODULE_: `app`
   - _PYTHON OBJECT_: `app.server`
   - _ENVIRONMENTS_: select `latest mlflow` from the dropdown

   and the click _SAVE_.
   
1. Click _START APP_ and wait until it shows _RUNNING_. Then your app is ready to use.

### Cleanup

Please stop the app when you're done with your exercise.


# Credits

- [Linear regression chart using Altair]( https://altair-viz.github.io/user_guide/transform/regression.html). This demo
  uses a modified example from this article.
- [Data](https://github.com/Kaushik-Varma/linear_regression_model_python/blob/main/Company_data.csv)
