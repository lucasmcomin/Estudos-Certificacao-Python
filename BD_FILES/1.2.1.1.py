import sqlite3


class Todo():

    def __init__(self, bd_name):

        self.conn = sqlite3.connect(bd_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    
    def create_table(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY, 
                                                                name TEXT NOT NULL, 
                                                                priority INTEGER NOT NULL);''')

    def find_task_by_name(self, name):
        nomes =  self.cursor.execute('SELECT name FROM Tasks')
        for nome in nomes:
            
            if nome[0].lower() == name.lower():
                return True

        return False        
                    

    def find_task_by_id(self, id_user):
        ids =  self.cursor.execute('SELECT id FROM Tasks')
        for id in ids:
            
            if id[0] == id_user:
                return True

        return False      

    def show_tasks(self):
        tasks =  self.cursor.execute('SELECT * FROM Tasks')

        for task in tasks:
            print(task)


    def add_task(self):
        while True:
            name = input("Digite o nome da tarefa: ")
            if name != "" and not self.find_task_by_name(name):
                while True:
                    try:
                        priority = int(input("Digite o nível de Prioridade: "))
                    except ValueError:
                        print("Valor incorreto, por favor digite um número")
                    else:
                        
                        if priority > 0:
                            self.cursor.execute('INSERT INTO Tasks (name, priority) VALUES(?,?)', (name, priority))
                            self.conn.commit()
                            break
                        else:
                            print("Digite um número de prioridade válido")
                break
            else:
                if not self.find_task(name):
                    print("Digite um nome válido")   
                else: 
                    print("Nome já inserido no banco de dados")

    
    
    def change_priority(self):
        while True:
            try:
                id = int(input("Informe o ID: "))
                priority = int(input("Informe o número de prioridade: "))
            except ValueError:
                print("Valor incorreto, por favor digite um número")
            else:
                if self.find_task_by_id(id):
                    self.conn.execute('''UPDATE Tasks SET priority = ? WHERE id = ?''', (priority, id))
                    break
                else:
                    print("ID não encontrado em nosso Banco de Dados")


    def delete_task(self):

        while True:
            try:
                id = int(input("Informe o ID: "))
            except ValueError:
                print("Valor incorreto, por favor digite um número")
            else:
                if self.find_task_by_id(id):
                    self.conn.execute('''DELETE FROM Tasks WHERE id = ?''', (id,))
                    break
                else:
                    print("ID não encontrado em nosso Banco de Dados")

    def close(self):
        self.conn.close()





def menu():
    todo = Todo("todo.bd")

    while True:
        print("------------------------")
        print("Please select one option")
        print("------------------------")
        print("1. - Listar Tarefas")
        print("2. - Adicionar Tarefas")
        print("3. - Mudar prioridade")
        print("4. - Deletar Tarefa")
        print("5. - Sair")
        print("------------------------")

        op = input("opção: ")

        match op:
            case "1":
                todo.show_tasks()
            case "2":
                todo.add_task()
            case "3":
                todo.change_priority()
            case "4":
                todo.delete_task()
            case "5":
                todo.close()
                exit()
                



menu()