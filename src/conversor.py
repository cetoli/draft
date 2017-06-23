# -*- coding: UTF8 -*-

from Tkinter import *
import tkMessageBox
import Tkinter, Tkconstants, tkFileDialog
import shapefile


class Aplicativo:
    def __init__(self, master):

        self.coordenadas = []
        self.campo = ''
        self.arqkml = self.salvar_kml

        # Meus frames
        self.frame1 = Frame(master)
        self.frame1.pack(side=LEFT, fill=BOTH, expand=1)

        self.frame2 = Frame(master)
        self.frame2.pack(side=RIGHT, fill=BOTH, expand=1)

        # widgets do Frame 1

        self.lb_texto = Label(self.frame1, text="CONVERTER SHAPEFILE EM KML/KMZ?", font=('Arial', 10, 'bold'),
                              fg='blue')
        self.lb_texto.grid(row=5, column=20)

        self.lb1 = Label(self.frame1, text="Input Shapefile", font=('Verdana', 10))
        self.lb1.grid(row=10, column=10)

        self.lb1_1 = Label(self.frame1, text="Output KML", font=('Verdana', 10))
        self.lb1_1.grid(row=30, column=10)

        self.ent1 = Entry(self.frame1, font=('Verdana', 10))  # entry do input
        self.ent1.grid(row=10, column=20)

        self.ent1_1 = Entry(self.frame1, font=('Verdana', 10))  # entry do output
        self.ent1_1.grid(row=30, column=20)

        self.bt1 = Button(self.frame1, text="Converte", font=('Verdana', 10),
                          command=self.lerShape)  # criar a função que irá converter o arquivo shape em kml
        self.bt1.grid(row=20, column=20)  # botao converter o arquivo em KML

        self.bt_abrir = Button(self.frame1, text="Abrir", font=('Verdana', 10),
                               command=self.abrir_shape)  # Função que abre o arquivo
        self.bt_abrir.grid(row=10, column=40)  # botao abrir arquivo shape

        self.bt_salvar = Button(self.frame1, text="Salvar", font=('Verdana', 10),
                                command=None)  # Função que salva arquivo convertido em KML
        self.bt_salvar.grid(row=30, column=40)  # botao abrir arquivo shape

        self.msg1 = Message(self.frame1,
                            text='')  # mensagem gerada quando o arquivo é inválido. Isso na função abrir_shape
        self.msg1.grid(row=10, column=30)

        self.msg1_1 = Message(self.frame1,
                              text='')  # mensagem gerada quando o arquivo é Salvo. Isso na função Salvar_kml
        self.msg1_1.grid(row=30, column=30)

        # Widget do Frame 2

        self.lb_texto = Label(self.frame2, text="CONVERTER KML/KMZ EM SHAPEFILE?", font=('Arial', 10, 'bold'),
                              fg='blue')
        self.lb_texto.grid(row=5, column=20)

        self.lb2 = Label(self.frame2, text="Input KMZ", font=('Verdana', 10))
        self.lb2.grid(row=10, column=10)

        self.lb1_2 = Label(self.frame2, text="Output Shapefile", font=('Verdana', 10))
        self.lb1_2.grid(row=30, column=10)

        self.ent2 = Entry(self.frame2, font=('Verdana', 10))  # entry do input
        self.ent2.grid(row=10, column=20)

        self.ent2_2 = Entry(self.frame2, font=('Verdana', 10))  # entry do output
        self.ent2_2.grid(row=30, column=20)

        self.bt2 = Button(self.frame2, text="Converte", font=('Verdana', 10),
                          command=None)  # criar a função que irá converter o arquivo shape em kml
        self.bt2.grid(row=20, column=20)  # botao converter o arquivo em KML

        self.bt_abrir = Button(self.frame2, text="Abrir", font=('Verdana', 10),
                               command=self.abrir_shape)  # Função que abre o arquivo
        self.bt_abrir.grid(row=10, column=40)  # botao abrir arquivo shape

        self.bt_salvar = Button(self.frame2, text="Salvar", font=('Verdana', 10),
                                command=None)  # Função que salva arquivo convertido em KML
        self.bt_salvar.grid(row=30, column=40)  # botao abrir arquivo shape

        self.msg2 = Message(self.frame2,
                            text='')  # mensagem gerada quando o arquivo é inválido. Isso na função abrir_shape
        self.msg2.grid(row=10, column=30)

        self.msg2_2 = Message(self.frame2,
                              text='')  # mensagem gerada quando o arquivo é Salvo. Isso na função Salvar_kml
        self.msg2_2.grid(row=30, column=30)

    def lerShape(self):
        arquivo_shape = self.abrir_shape()

    def salvarKML(self): #Questão 9 que ele deu para a  P1

        # salva=tkFileDialog.asksaveasfilename()
        arqkml= file("/home/carlo/Documentos/dev/draft/src/pnts_shape.kml",'w')
        # Escrevendo o inicio do arquivo KML. Lembre que \n eh quebra de
        # linha e \t eh tabulacao
        self.arqkml=arqkml  #  file(self.salvar_kml,'w')
        self.arqkml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        self.arqkml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        self.arqkml.write('\t<Document>\n')
        self.arqkml.write('\t\t<name>Exportando coordenadas em Python</name>\n')
        # Agora o looping para escrever cada coordenadas
        cont = 0
        for c in self.coordenadas:
            print("point", c)
            cont += 1
            self.arqkml.write('\t\t<Placemark>\n')
            self.arqkml.write('\t\t\t<name>Coordenada '+str(cont)+'</name>\n')
            self.arqkml.write('\t\t\t<Point>\n')
            self.arqkml.write('\t\t\t\t<coordinates>'+str(c[0][0])+','+str(c[0][1])+'</coordinates>\n')
            self.arqkml.write('\t\t\t</Point>\n\t\t</Placemark>')
        # para fechar a estrutura do arquivo
        self.arqkml.write('\t</Document>\n</kml>')
        self.arqkml.close() # para garantir a escrita...
    

    # SAI DO PROGRAMA
    def sair(self):
        if tkMessageBox.askokcancel("Sair", "Deseja realmente sair?"):
            self.master.destroy()


            # ABRE ARQUIVOS SHAPES

    def abrir_shape(self):
        try:

            # self.frame1.filename = tkFileDialog.askopenfilename()
            self.frame1.filename = "/home/carlo/Documentos/dev/draft/src/pnts_shape.shp"
            print (self.frame1.filename)
            arquivo_shape = shapefile.Reader(self.frame1.filename, 'rb')
            self.campo = arquivo_shape.shapes()
            self.coordenadas = [sp.points for sp in self.campo]
            print self.coordenadas

        except Exception:  # Essa exceção foi colocado, pois não tinha outro

            self.msg1.configure(text="Arquivo Inválido")

        self.ent1.insert(0, self.frame1.filename)

    # ABRE ARQUIVOS KML
    def abrir_kml(self):  # refazer esse
        try:

            self.master.filename = tkFileDialog.askopenfilename()
            print (self.master.filename)
            arquivo_shape = shapefile.Reader(self.master.filename, 'rb')

        except Exception:  # Essa exceção foi colocado, pois não tinha outro

            self.msg2.configure(text="Arquivo Inválido")

        self.ent2.insert(0, self.master.filename)

    # ARQUIVO SHAPE SALVO quando faz a conversão de kml para shape.
    def salvar_shape(self):

        arquivo = shapefile.Writer(shapeType=1)
        salva = arquivo.save(tkFileDialog.asksaveasfilename())

        self.msg2_2.configure(text="Arquivo Salvo")
        self.ent2_2.insert(0, arquivo.save())
        print (salva)

    # ARQUIVO KML SALVO quando faz a conversão de shape para kml.
    def salvar_kml(self):  # refazer essa função

        arquivo = shapefile.Writer(shapeType=1)
        # salva = arquivo.save(tkFileDialog.asksaveasfilename())
        salva = "/home/carlo/Documentos/dev/draft/src/pnts_shape.kml"

        self.msg1_1.configure(text="Arquivo Salvo")
        self.ent1_1.insert(0, arquivo.save())
        print (salva)


janela = Tk()
janela.title('Conversor de Shape em KML e de KML em Shape')
janela.geometry('900x250')
app = Aplicativo(janela)
app.abrir_shape()
app.salvarKML()
#janela.mainloop()