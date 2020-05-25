db.auth("$MONGO_INITDB_ROOT_USERNAME", "$MONGO_INITDB_ROOT_PASSWORD")

db.createUser(
    {
        user: "$DB_USER",
        pwd: "$DB_PASSWORD",
        roles: [
            {
                role: "readWrite",
                db: "$MONGO_INITDB_DATABASE"
            }
        ]
    }
);
