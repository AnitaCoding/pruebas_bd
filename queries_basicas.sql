/*seleccionar todos los registros de una tabla*/
SELECT * FROM persona;
/*seleccionar algunos campos de una tabla*/
SELECT name, lastname FROM persona;
/*insertar resgistros nuevos*/
INSERT INTO persona (name, lastname, dni, email) VALUES ("Fernando", "Guerrero", "54888777D", "elfer@gmail.com");
/*actualizar registros de la tabla, si no le pasamos where, actualiza todos los registros, hay que pasarle la clave única*/
UPDATE persona SET name="Marta", lastname="Zurdo", dni="77555444X", email="mz@hotmail.com" WHERE id=3;
/*en consultas con filtros también usamos where. con like buscaríamos algo parecido where nanana like nanana*/
SELECT * FROM persona WHERE name="Mónica";
SELECT * FROM persona ORDER BY id DESC;
/*borrar registro. IMPORTANTE USAR WHERE o borramos todos los registros*/
DELETE FROM persona WHERE id = 2;