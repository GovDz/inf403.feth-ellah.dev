from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'db.db'

# Function to establish database connection
def connect_db():
    return sqlite3.connect(DATABASE)

# Function to execute SQL quer  ies
def execute_query(query, args=()):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to display all products
@app.route('/products')
def show_products():
    query = "SELECT * FROM Product"
    products = execute_query(query)
    return render_template('product.html', products=products)

# Route for the main menu
@app.route('/main_menu', methods=['GET', 'POST'])
def menu_option():
    if request.method == 'POST':
        option = request.form['option']
        if option == 'show_tables':
            # Add code to show tables
            return redirect(url_for('show_tables'))
        elif option == 'show_rows':
            # Add code to show rows
            return redirect(url_for('show_rows'))
        elif option == 'update_tables':
            # Add code to update tables
            return redirect(url_for('update_menu'))
        elif option == 'tools':
            # Add code for tools
            return redirect(url_for('tools'))
        elif option == 'exit':
            return redirect(url_for('index'))  # Redirect to the main page
    return render_template('main_menu.html')


@app.route('/update_menu', methods=['GET', 'POST'])
def update_menu():
    if request.method == 'POST':
        option = request.form['option']
        if option == 'Add_row':
            return redirect(url_for('add_row'))
        elif option == 'Update_row':
            return redirect(url_for('update_row'))
        elif option == 'Remove_row':
            return redirect(url_for('remove_row'))
        elif option == 'Return':
            return redirect(url_for('menu_option'))
    return render_template('update_menu.html')

@app.route('/Add_row', methods=['GET', 'POST'])
def add_row():
    if request.method == 'POST':
        table_name = request.form['table_name']
        return redirect(url_for(f'add_row_{table_name.lower()}'))  # Redirect to the appropriate add_row page
    else:
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = [table[0] for table in execute_query(query)]  # Extract table names from tuples
        return render_template('select_tables_add.html', tables=tables)

@app.route('/add_row_<table_name>', methods=['GET', 'POST'])
def add_row_table(table_name):
    if request.method == 'POST':
        return redirect(url_for('menu_option'))  # Redirect to the main menu after adding the row
    else:
        return render_template(f'add_row_{table_name.lower()}.html')  # Render the add row form for the specified table


@app.route('/add_row_order')
def add_row_order():
    if request.method == 'POST':
        return redirect(url_for('menu_option'))  # Redirect to the main menu after adding the row
    else:
        return render_template('add_row_order.html')  # Render the add row form for the 'Order' table
 

@app.route('/tools', methods=['GET', 'POST'])
def tools():
    if request.method == 'POST':
        option = request.form.get('option')
        if option == 'perform_custom_sql_query':
            # Perform custom SQL query function
            return render_template('custom_sql_query.html')
        elif option == 'customer_by_id':
            # Fetch customer by ID function
            return render_template('customer_by_id.html')
        elif option == 'product_by_id':
            # Fetch product by ID function
            return render_template('product_by_id.html')
        elif option == 'order_by_id':
            # Fetch order by ID function
            return render_template('order_by_id.html')
        elif option == 'warehouse_by_id':
            # Fetch warehouse by ID function
            return render_template('warehouse_by_id.html')
        elif option == 'recycling_company_by_id':
            # Fetch recycling company by ID function
            return render_template('recycling_company_by_id.html')
        elif option == 'city_by_postal_code':
            # Fetch city by postal code function
            return render_template('city_by_postal_code.html')
        elif option == 'orders_by_product_id':
            # Fetch orders by product ID function
            return render_template('orders_by_product_id.html')
        elif option == 'products_by_customer_id':
            # Fetch products by customer ID function
            return render_template('products_by_customer_id.html')
        elif option == 'orders_by_city':
            # Fetch orders by city function
            return render_template('orders_by_city.html')
        elif option == 'orders_by_date_range':
            # Fetch orders by date range function
            return render_template('orders_by_date_range.html')
        elif option == 'customers_by_order_date':
            # Fetch customers by order date function
            return render_template('customers_by_order_date.html')
        elif option == 'products_by_waste_type':
            # Fetch products by waste type function
            return render_template('products_by_waste_type.html')
        elif option == 'orders_by_recycling_company':
            # Fetch orders by recycling company function
            return render_template('orders_by_recycling_company.html')
        elif option == 'orders_by_warehouse':
            # Fetch orders by warehouse function
            return render_template('orders_by_warehouse.html')
        elif option == 'orders_by_city':
            # Fetch orders by city function
            return render_template('orders_by_city.html')
        elif option == 'orders_by_product_type':
            # Fetch orders by product type function
            return render_template('orders_by_product_type.html')
        elif option == 'orders_by_product_waste_type':
            # Fetch orders by product waste type function
            return render_template('orders_by_product_waste_type.html')
        elif option == 'orders_by_product_name':
            # Fetch orders by product name function
            return render_template('orders_by_product_name.html')
        elif option == 'orders_by_product_id':
            # Fetch orders by product ID function
            return render_template('orders_by_product_id.html')
        elif option == 'orders_by_customer_id':
            # Fetch orders by customer ID function
            return render_template('orders_by_customer_id.html')
        elif option == 'orders_by_customer_name':
            # Fetch orders by customer name function
            return render_template('orders_by_customer_name.html')
        elif option == 'customers_by_product_id':
            # Fetch customers by product ID function
            return render_template('customers_by_product_id.html')
        elif option == 'customers_by_product_name':
            # Fetch customers by product name function
            return render_template('customers_by_product_name.html')
        elif option == 'customers_by_city':
            # Fetch customers by city function
            return render_template('customers_by_city.html')
        elif option == 'customers_by_order_date_range':
            # Fetch customers by order date range function
            return render_template('customers_by_order_date_range.html')
        elif option == 'products_by_customer_id':
            # Fetch products by customer ID function
            return render_template('products_by_customer_id.html')
        elif option == 'products_by_customer_name':
            # Fetch products by customer name function
            return render_template('products_by_customer_name.html')
        elif option == 'products_by_customer_city':
            # Fetch products by customer city function
            return render_template('products_by_customer_city.html')
        elif option == 'products_by_customer_order_date_range':
            # Fetch products by customer order date range function
            return render_template('products_by_customer_order_date_range.html')
        elif option == 'products_by_customer_type':
            # Fetch products by customer type function
            return render_template('products_by_customer_type.html')
        elif option == 'products_by_customer_waste_type':
            # Fetch products by customer waste type function
            return render_template('products_by_customer_waste_type.html')
        elif option == 'products_by_customer_id_and_date_range':
            # Fetch products by customer ID and date range function
            return render_template('products_by_customer_id_and_date_range.html')
        elif option == 'products_by_customer_name_and_date_range':
            # Fetch products by customer name and date range function
            return render_template('products_by_customer_name_and_date_range.html')
        elif option == 'products_by_customer_city_and_date_range':
            # Fetch products by customer city and date range function
            return render_template('products_by_customer_city_and_date_range.html')
        elif option == 'products_by_customer_type_and_date_range':
            # Fetch products by customer type and date range function
            return render_template('products_by_customer_type_and_date_range.html')
        elif option == 'products_by_customer_waste_type_and_date_range':
            # Fetch products by customer waste type and date range function
            return render_template('products_by_customer_waste_type_and_date_range.html')
        elif option == 'customers_by_product_id_and_date_range':
            # Fetch customers by product ID and date range function
            return render_template('customers_by_product_id_and_date_range.html')
        elif option == 'customers_by_product_name_and_date_range':
            # Fetch customers by product name and date range function
            return render_template('customers_by_product_name_and_date_range.html')
        elif option == 'customers_by_city_and_date_range':
            # Fetch customers by city and date range function
            return render_template('customers_by_city_and_date_range.html')
        elif option == 'customers_by_product_type_and_date_range':
            # Fetch customers by product type and date range function
            return render_template('customers_by_product_type_and_date_range.html')
        elif option == 'customers_by_product_waste_type_and_date_range':
            # Fetch customers by product waste type and date range function
            return render_template('customers_by_product_waste_type_and_date_range.html')
        elif option == 'orders_by_warehouse_and_date_range':
            # Fetch orders by warehouse and date range function
            return render_template('orders_by_warehouse_and_date_range.html')
        elif option == 'orders_by_recycling_company_and_date_range':
            # Fetch orders by recycling company and date range function
            return render_template('orders_by_recycling_company_and_date_range.html')
        elif option == 'orders_by_city_and_date_range':
            # Fetch orders by city and date range function
            return render_template('orders_by_city_and_date_range.html')
        elif option == 'orders_by_product_type_and_date_range':
            # Fetch orders by product type and date range function
            return render_template('orders_by_product_type_and_date_range.html')
        elif option == 'orders_by_product_waste_type_and_date_range':
            # Fetch orders by product waste type and date range function
            return render_template('orders_by_product_waste_type_and_date_range.html')
        elif option == 'orders_by_product_name_and_date_range':
            # Fetch orders by product name and date range function
            return render_template('orders_by_product_name_and_date_range.html')
        elif option == 'orders_by_product_id_and_date_range':
            # Fetch orders by product ID and date range function
            return render_template('orders_by_product_id_and_date_range.html')
        elif option == 'orders_by_customer_id_and_date_range':
            # Fetch orders by customer ID and date range function
            return render_template('orders_by_customer_id_and_date_range.html')
        elif option == 'orders_by_customer_name_and_date_range':
            # Fetch orders by customer name and date range function
            return render_template('orders_by_customer_name_and_date_range.html')
        elif option == 'tools':
            # Reload the tools page
            return render_template('tools.html')
        else:
            # Handle invalid options
            return render_template('invalid_option.html')
    return render_template('tools.html')

def execute_custom_sql_query(query):
    # Connect to the SQLite database
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all rows
    except Exception as e:
        result = str(e)
    finally:
        cursor.close()
        conn.close()
    return result

# Route for custom SQL query form
@app.route('/custom_sql_query', methods=['GET', 'POST'])
def custom_sql_query():
    if request.method == 'POST':
        query = request.form['query']
        # Check if the query contains any harmful keywords
        if any(keyword in query.lower() for keyword in ['delete', 'drop', 'truncate']):
            abort(403)  # Forbidden: User attempted a harmful operation
        result = execute_custom_sql_query(query)
        # Convert result list to a string without "result=" prefix
        result_string = '&'.join(str(row) for row in result)
        return redirect(url_for('custom_sql_query_result', result=result_string))
    return render_template('custom_sql_query.html')

# Route for displaying custom SQL query results
@app.route('/custom_sql_query/result')
def custom_sql_query_result():
    # Get the query result from the URL parameter
    result_string = request.args.get('result')
    # Split the result string into individual results and remove "result="
    results = [result.replace('result=', '') for result in result_string.split('&')]
    return render_template('custom_sql_query_result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/add_row_city', methods=['GET'])
def add_row_city_form():
    return render_template('add_row_city.html')

# Route to handle the form submission and insert a new row into the 'City' table
@app.route('/add_row_city', methods=['POST'])
def add_row_city():
    if request.method == 'POST':
        city_name = request.form['city_name']
        postal_code = request.form['postal_code']
        id_company = request.form.get('id_company') 
        query = "INSERT INTO City (postal_code, city_name, id_company) VALUES (?,?,?);"
        execute_query(query, (postal_code, city_name, id_company))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after adding the row


@app.route('/add_row_product', methods=['GET', 'POST'])
def add_row_product():
    if request.method == 'POST':
        waste = request.form['waste']
        # Assuming you have a function to get the id_product based on the waste
        id_product = get_product_id_by_waste(waste)
        # Assuming you have a function to insert a new row into the Product table
        execute_query("INSERT INTO Product (id_product, waste) VALUES (?, ?);", (id_product, waste))
        return redirect(url_for('menu_option'))
    else:
        return render_template('add_row_product.html')

@app.route('/add_row_recycling_company', methods=['GET', 'POST'])
def add_row_recycling_company():
    if request.method == 'POST':
        comp_name = request.form['comp_name']
        # Assuming you have a function to insert a new row into the Recycling_Company table
        execute_query("INSERT INTO Recycling_Company (comp_name) VALUES (?);", (comp_name,))
        return redirect(url_for('menu_option'))
    else:
        return render_template('add_row_recyco.html')

@app.route('/add_row_companyproduct', methods=['GET', 'POST'])
def add_row_companyproduct():
    if request.method == 'POST':
        id_company = request.form['id_company']
        id_product = request.form['id_product']
        execute_query("INSERT INTO CompanyProduct (id_company, id_product) VALUES (?, ?);", (id_company, id_product))
        return redirect(url_for('menu_option'))
    else:
        return render_template('add_row_compro.html')

@app.route('/add_row_warehouse', methods=['GET', 'POST'])
def add_row_warehouse():
    if request.method == 'POST':
        name_warehouse = request.form['name_warehouse']
        waste = request.form['waste']
        id_company = request.form['id_company']
        # Assuming you have a function to insert a new row into the Warehouse table
        execute_query("INSERT INTO Warehouse (name_warehouse, waste, id_company) VALUES (?, ?, ?);", (name_warehouse, waste, id_company))
        return redirect(url_for('menu_option'))
    else:
        return render_template('add_row_warehouse.html')

@app.route('/add_row_customer', methods=['GET', 'POST'])
def add_row_customer():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_phone = request.form['customer_phone']
        country = request.form['country']
        # Assuming you have a function to insert a new row into the Customer table
        execute_query("INSERT INTO Customer (customer_name, customer_phone, country) VALUES (?, ?, ?);", (customer_name, customer_phone, country))
        return redirect(url_for('menu_option'))
    else:
        return render_template('add_row_customer.html')

@app.route('/add_row_orders', methods=['GET', 'POST'])
def add_row_orders():
    if request.method == 'POST':
        id_customer = request.form['id_customer']
        id_product = request.form['id_product']
        order_date = request.form['order_date']
        # Assuming you have a function to insert a new row into the Orders table
        execute_query("INSERT INTO Orders (id_customer, id_product, order_date) VALUES (?, ?, ?);", (id_customer, id_product, order_date))
        return redirect(url_for('menu_option'))
    else:
        return render_template('add_row_orders.html')

# Route to display form for selecting table for row removal
@app.route('/remove_row', methods=['GET', 'POST'])
def remove_row():
    if request.method == 'POST':
        table_name = request.form['table_name']
        return redirect(url_for(f'remove_row_{table_name.lower()}_form'))  # Redirect to the form for specifying conditions for row removal
    else:
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = [table[0] for table in execute_query(query)]  # Extract table names from tuples
        return render_template('select_tables_remove.html', tables=tables)



# Route to display form for specifying conditions to remove rows from the 'City' table
@app.route('/remove_row_city', methods=['GET'])
def remove_row_city_form():
    return render_template('remove_row_city.html')

# Route to handle the form submission and delete rows from the 'City' table based on specified conditions
@app.route('/remove_row_city', methods=['POST'])
def remove_row_city():
    if request.method == 'POST':
        postal_code = request.form['postal_code']
        # Construct the DELETE query to remove rows based on the specified postal code
        query = "DELETE FROM City WHERE postal_code = ?;"
        execute_query(query, (postal_code,))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after removing the row

# Route and function for displaying form to specify conditions for row removal from the 'Recycling_Company' table
@app.route('/remove_row_recycling_company_form', methods=['GET'])
def remove_row_recycling_company_form():
    return render_template('remove_row_recycling_company.html')

# Route and function for handling row removal from the 'Recycling_Company' table based on specified conditions
@app.route('/remove_row_recycling_company', methods=['POST'])
def remove_row_recycling_company():
    if request.method == 'POST':
        id_company = request.form['id_company']
        query = "DELETE FROM Recycling_Company WHERE id_company = ?;"
        execute_query(query, (id_company,))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after removing the row


# Route and function for displaying form to specify conditions for row removal from the 'CompanyProduct' table
@app.route('/remove_row_companyproduct_form', methods=['GET'])
def remove_row_companyproduct_form():
    return render_template('remove_row_company_product.html')

# Route and function for handling row removal from the 'CompanyProduct' table based on specified conditions
@app.route('/remove_row_companyproduct', methods=['POST'])
def remove_row_companyproduct():
    if request.method == 'POST':
        id_company = request.form['id_company']
        id_product = request.form['id_product']
        query = "DELETE FROM CompanyProduct WHERE id_company = ? AND id_product = ?;"
        execute_query(query, (id_company, id_product))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after removing the row


# Route and function for displaying form to specify conditions for row removal from the 'Warehouse' table
@app.route('/remove_row_warehouse_form', methods=['GET'])
def remove_row_warehouse_form():
    return render_template('remove_row_warehouse.html')

# Route and function for handling row removal from the 'Warehouse' table based on specified conditions
@app.route('/remove_row_warehouse', methods=['POST'])
def remove_row_warehouse():
    if request.method == 'POST':
        id_warehouse = request.form['id_warehouse']
        query = "DELETE FROM Warehouse WHERE id_warehouse = ?;"
        execute_query(query, (id_warehouse,))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after removing the row


# Route and function for displaying form to specify conditions for row removal from the 'Customer' table
@app.route('/remove_row_customer_form', methods=['GET'])
def remove_row_customer_form():
    return render_template('remove_row_customer.html')

# Route and function for handling row removal from the 'Customer' table based on specified conditions
@app.route('/remove_row_customer', methods=['POST'])
def remove_row_customer():
    if request.method == 'POST':
        id_customer = request.form['id_customer']
        query = "DELETE FROM Customer WHERE id_customer = ?;"
        execute_query(query, (id_customer,))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after removing the row


# Route and function for displaying form to specify conditions for row removal from the 'Orders' table
@app.route('/remove_row_orders_form', methods=['GET'])
def remove_row_orders_form():
    return render_template('remove_row_orders.html')

# Route and function for handling row removal from the 'Orders' table based on specified conditions
@app.route('/remove_row_orders', methods=['POST'])
def remove_row_orders():
    if request.method == 'POST':
        id_customer = request.form['id_customer']
        id_product = request.form['id_product']
        order_date = request.form['order_date']
        query = "DELETE FROM Orders WHERE id_customer = ? AND id_product = ? AND order_date = ?;"
        execute_query(query, (id_customer, id_product, order_date))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after removing the row

# Route and function for displaying form to specify conditions for row removal from the 'Product' table
@app.route('/remove_row_product_form', methods=['GET'])
def remove_row_product_form():
    return render_template('remove_row_product.html')

# Route and function for handling row removal from the 'Product' table based on specified conditions
@app.route('/remove_row_product', methods=['POST'])
def remove_row_product():
    if request.method == 'POST':
        id_product = request.form['id_product']
        query = "DELETE FROM Product WHERE id_product = ?;"
        execute_query(query, (id_product,))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after removing the row

# Similarly, add routes and functions for removing rows from other tables like Recycling_Company, CompanyProduct, Warehouse, Customer, and Orders

# Route to display form for selecting table for row update
@app.route('/update_row', methods=['GET', 'POST'])
def update_row():
    if request.method == 'POST':
        table_name = request.form['table_name']
        return redirect(url_for(f'update_row_{table_name.lower()}_form'))  # Redirect to the form for updating rows in the selected table
    else:
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = [table[0] for table in execute_query(query)]  # Extract table names from tuples
        return render_template('select_tables_update.html', tables=tables)

# Route and function for displaying form to update rows in the 'City' table
@app.route('/update_row_city_form', methods=['GET'])
def update_row_city_form():
    return render_template('update_row_city.html')

# Route and function for handling row update in the 'City' table
@app.route('/update_row_city', methods=['POST'])
def update_row_city():
    if request.method == 'POST':
        postal_code = request.form['postal_code']
        city_name = request.form['city_name']
        id_company = request.form['id_company']
        query = "UPDATE City SET city_name = ?, id_company = ? WHERE postal_code = ?;"
        execute_query(query, (city_name, id_company, postal_code))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after updating the row
# Route and function for displaying form to update rows in the 'Product' table
@app.route('/update_row_product_form', methods=['GET'])
def update_row_product_form():
    return render_template('update_row_product.html')

# Route and function for handling row update in the 'Product' table
@app.route('/update_row_product', methods=['POST'])
def update_row_product():
    if request.method == 'POST':
        id_product = request.form['id_product']
        waste = request.form['waste']
        query = "UPDATE Product SET waste = ? WHERE id_product = ?;"
        execute_query(query, (waste, id_product))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after updating the row

# Route and function for displaying form to update rows in the 'Recycling_Company' table
@app.route('/update_row_recycling_company_form', methods=['GET'])
def update_row_recycling_company_form():
    return render_template('update_row_recycling_company.html')

# Route and function for handling row update in the 'Recycling_Company' table
@app.route('/update_row_recycling_company', methods=['POST'])
def update_row_recycling_company():
    if request.method == 'POST':
        id_company = request.form['id_company']
        comp_name = request.form['comp_name']
        query = "UPDATE Recycling_Company SET comp_name = ? WHERE id_company = ?;"
        execute_query(query, (comp_name, id_company))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after updating the row
# Route and function for displaying form to update rows in the 'CompanyProduct' table
@app.route('/update_row_companyproduct_form', methods=['GET'])
def update_row_companyproduct_form():
    return render_template('update_row_companyproduct.html')

# Route and function for handling row update in the 'CompanyProduct' table
@app.route('/update_row_companyproduct', methods=['POST'])
def update_row_companyproduct():
    if request.method == 'POST':
        id_company = request.form['id_company']
        id_product = request.form['id_product']
        query = "UPDATE CompanyProduct SET id_product = ? WHERE id_company = ?;"
        execute_query(query, (id_product, id_company))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after updating the row
# Route and function for displaying form to update rows in the 'Warehouse' table
@app.route('/update_row_warehouse_form', methods=['GET'])
def update_row_warehouse_form():
    return render_template('update_row_warehouse.html')

# Route and function for handling row update in the 'Warehouse' table
@app.route('/update_row_warehouse', methods=['POST'])
def update_row_warehouse():
    if request.method == 'POST':
        id_warehouse = request.form['id_warehouse']
        name_warehouse = request.form['name_warehouse']
        waste = request.form['waste']
        id_company = request.form['id_company']
        query = "UPDATE Warehouse SET name_warehouse = ?, waste = ?, id_company = ? WHERE id_warehouse = ?;"
        execute_query(query, (name_warehouse, waste, id_company, id_warehouse))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after updating the row
# Route and function for displaying form to update rows in the 'Customer' table
@app.route('/update_row_customer_form', methods=['GET'])
def update_row_customer_form():
    return render_template('update_row_customer.html')

# Route and function for handling row update in the 'Customer' table
@app.route('/update_row_customer', methods=['POST'])
def update_row_customer():
    if request.method == 'POST':
        id_customer = request.form['id_customer']
        customer_name = request.form['customer_name']
        customer_phone = request.form['customer_phone']
        country = request.form['country']
        query = "UPDATE Customer SET customer_name = ?, customer_phone = ?, country = ? WHERE id_customer = ?;"
        execute_query(query, (customer_name, customer_phone, country, id_customer))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after updating the row
# Route and function for displaying form to update rows in the 'Orders' table
@app.route('/update_row_orders_form', methods=['GET'])
def update_row_orders_form():
    return render_template('update_row_orders.html')

# Route and function for handling row update in the 'Orders' table
@app.route('/update_row_orders', methods=['POST'])
def update_row_orders():
    if request.method == 'POST':
        id_customer = request.form['id_customer']
        id_product = request.form['id_product']
        order_date = request.form['order_date']
        query = "UPDATE Orders SET id_product = ?, order_date = ? WHERE id_customer = ?;"
        execute_query(query, (id_product, order_date, id_customer))
        return redirect(url_for('menu_option'))  # Redirect to the main menu after updating the row


@app.route('/show_tables')
def show_tables():
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = execute_query(query)
    return render_template('show_tables.html', tables=tables)
    

def get_rows(table_name):
    conn = connect_db()
    cur = conn.cursor()
    query = f"SELECT * FROM {table_name};"
    cur.execute(query)
    columns = [description[0] for description in cur.description]  # Extract column names
    rows = cur.fetchall()
    conn.close()
    return columns, rows

# Route to show rows
@app.route('/show_rows', methods=['GET', 'POST'])
def show_rows():
    if request.method == 'POST':
        table_name = request.form['table_name']
        columns, rows = get_rows(table_name)
        return render_template('show_rows.html', columns=columns, rows=rows)
    else:
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = [table[0] for table in execute_query(query)]  # Extract table names from tuples
        return render_template('select_table.html', tables=tables)

# Route for customer search
@app.route('/search_customers', methods=['POST'])
def search_customers():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    query = "SELECT * FROM Customer WHERE order_date BETWEEN ? AND ?"
    results = execute_query(query, (start_date, end_date))
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)