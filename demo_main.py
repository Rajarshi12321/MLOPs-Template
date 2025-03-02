from main_app_deploy.components.data_querying import my_query
import os

os.environ["LANGCHAIN_PROJECT"] = "GAME RECOMMENDATION"

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

ans = my_query("can you reccomend me some fantasy games? about 2 games")

print(ans)


echo "# h" >> README.md
git init

git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Rajarshi12321/Agentic-Career-Guide.git
git push -u origin main

git branch --set-upstream-to=origin/main main