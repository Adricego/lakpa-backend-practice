INSERT INTO clientes (id, nombre, email)
VALUES
    (1, 'Camila Rojas', 'camila.rojas@email.com'),
    (2, 'Pedro Soto', 'pedro.soto@email.com'),
    (3, 'Ana Torres', 'ana.torres@email.com')
ON CONFLICT (id) DO UPDATE
SET
    nombre = EXCLUDED.nombre,
    email = EXCLUDED.email;

INSERT INTO portafolios (id, cliente_id, nombre, valor_total, moneda)
VALUES
    (1, 1, 'Portafolio Conservador', 1500000.00, 'CLP'),
    (2, 2, 'Portafolio Balanceado', 2500000.00, 'CLP'),
    (3, 3, 'Portafolio Crecimiento', 3000000.00, 'CLP')
ON CONFLICT (id) DO UPDATE
SET
    cliente_id = EXCLUDED.cliente_id,
    nombre = EXCLUDED.nombre,
    valor_total = EXCLUDED.valor_total,
    moneda = EXCLUDED.moneda;

SELECT setval(
    pg_get_serial_sequence('clientes', 'id'),
    (SELECT MAX(id) FROM clientes)
);

SELECT setval(
    pg_get_serial_sequence('portafolios', 'id'),
    (SELECT MAX(id) FROM portafolios)
);