export AWS_USERNAME=postgres
export AWS_DBPASSWD=project3group00postgres
export AWS_DBNAME=project_3_group_00_db
export AWS_ENDPOINT=project-3-group-00.cmpk8jwwic92.us-east-2.rds.amazonaws.com

# This will combine the above information
export DATABASE_URL=postgresql://${AWS_USERNAME}:${AWS_DBPASSWD}@${AWS_ENDPOINT}:5432/${AWS_DBNAME}

#This will print the DATABASE_URL
echo ${DATABASE_URL}

#Verifies that it matches with above
python -c "import os; print(os.environ.get('DATABASE_URL', ''))"

#
python initdb.py