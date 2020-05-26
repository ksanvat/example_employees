#### === Simply usage ===

```bash
git clone ... <dir>
cd <dir>
docker-compose up -d
...
docker-compose down
```

- Browser api url: [http://localhost:8000/api/v1/employees/](http://localhost:8000/api/v1/employees/)
- Available query filters
    - [offset](http://localhost:8000/api/v1/employees/?offset=10): int
    - [limit](http://localhost:8000/api/v1/employees/?limit=30): int
    - [text](http://localhost:8000/api/v1/employees/?text=chester): str - search via 'name', 'company' and 'job_title'
    - [name](http://localhost:8000/api/v1/employees/?name=odge): str
    - [age](http://localhost:8000/api/v1/employees/?age=21) or [age_lt](http://localhost:8000/api/v1/employees/?age_lt=22), [age_gt](http://localhost:8000/api/v1/employees/?age_gt=22): int
    - [company](http://localhost:8000/api/v1/employees/?company=google): str
    - [job_title](http://localhost:8000/api/v1/employees/?job_title=director): str
    - [gender](http://localhost:8000/api/v1/employees/?gender=male): str


TODO:
- отдельные сериализаторы
- улучшить фильтры (eq, ne, lt, lte, gt, gte - сделать так, чтобы не нужно было каждый параметр прописывать руками)
- добавить конфиги test-stage + прикрутить nginx
- покрыть тестами
