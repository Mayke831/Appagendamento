from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de horários disponíveis
horarios = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
agendamentos = {}


@app.route("/")
def index():
    disponiveis = [h for h in horarios if h not in agendamentos]
    return render_template("index.html", horarios=disponiveis, agendamentos=agendamentos)


@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    horario = request.form.get("horario")

    if not nome or not telefone or not horario:
        return redirect(url_for("index"))

    if horario in agendamentos:
        return redirect(url_for("index"))

    agendamentos[horario] = {"nome": nome, "telefone": telefone}
    horarios.remove(horario)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
