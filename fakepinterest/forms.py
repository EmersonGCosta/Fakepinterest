# formularios do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, FileField
from  wtforms.validators import DataRequired, Email, Length, EqualTo,ValidationError
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("Email", validators= [DataRequired(), Email()] )
    senha = PasswordField ("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField ("Fazer Login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta")


class FormCriarConta(FlaskForm):
    email = StringField("Email", validators= [DataRequired(), Email()] )
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators= [DataRequired(), Length(2,15)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado, faça o login ou use outro email para continuar")

    # def validate_username(self, username):
    #     usuario = Usuario.query.filter_by(email = username.data).first()
    #     if usuario:
    #         raise ValidationError("Nome já cadastrado, faça o login ou use outro Nome para continuar")

class FormFoto (FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")