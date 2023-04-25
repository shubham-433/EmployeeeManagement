# Django Test
## Python Version 3.10
## CLI Commands
``` bash
# run following commands in terminal in backend_test directory 
# after cloning.

pip install pipenv
pipenv install
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
# this command could take some time to run
python manage.py create_employees
```

``` bash
# if below command ran without any errors, 
# it means you have installed this project successfully.
python manage.py runserver
```

## Task
``` bash
1. Make a relationship between companies and employees.
2. In home page there is a table with company names and an empty link along with each company. 
   clinking on that link, should open up a page to a form with a dropdwon of employees that when choosed 
   should associate that employee with that particular company and redrirect to the table.
3. All employee names associated with a company should be displayed comma separated on the second column of the table on the home page.
4. Each employee can only be associated with one company only.
5. Employee dropdown in the form should be searchable.

```
#home page
![image](https://user-images.githubusercontent.com/76087769/234353337-dc590335-cee5-40e7-8ba5-b043b11bf679.png)
# user can add employee to company
![image](https://user-images.githubusercontent.com/76087769/234353697-b48ed06d-3374-4519-b225-14dc0f3fe488.png)
# if employee does not belong to any compnay then add employee to selected comanpy and if user already have company then the replace the company
![image](https://user-images.githubusercontent.com/76087769/234354277-e8c455c0-4e1c-42d0-a25d-1b2cbde44913.png)
# user can also add new company 
![image](https://user-images.githubusercontent.com/76087769/234354191-2e93a79f-2f0a-4441-9f76-aa6c9bcc1081.png)
#user can also add new employee
![image](https://user-images.githubusercontent.com/76087769/234354441-2d902899-7e8a-43d3-a546-b96293d31578.png)


