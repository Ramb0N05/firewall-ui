from flask_babel import gettext as _
from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Optional, DataRequired, Email


class frm_user_profile(FlaskForm):
    first_name = StringField(
        _("First name"),
        validators=[DataRequired(message=_("Please input your first name"))],
        render_kw={"placeholder": _("First Name")},
    )
    last_name = StringField(
        _("Last name"),
        validators=[Optional()],
        render_kw={"placeholder": _("Last Name")},
    )
    email = StringField(
        _("Email"),
        validators=[Email(message=_("Not a valid email address.")), DataRequired()],
        render_kw={"placeholder": _("Email")},
    )
    gravatar_url = StringField(
        _("Gravatar url"),
        validators=[Optional()],
        render_kw={"placeholder": _("URI")},
    )
    submit = SubmitField(_("Save"))
