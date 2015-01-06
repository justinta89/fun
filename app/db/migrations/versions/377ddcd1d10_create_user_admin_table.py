"""create user_admin table

Revision ID: 377ddcd1d10
Revises: 4ff71afbdbd
Create Date: 2014-04-28 08:56:57.157482

"""

# revision identifiers, used by Alembic.
revision = '377ddcd1d10'
down_revision = '4ff71afbdbd'

from alembic import op
from sqlalchemy import Column, String, Integer, DateTime


def upgrade():
    op.create_table('useradmin',
                    Column('id', Integer, primary_key=True),
                    Column('username', String(24),
                           unique=True,
                           nullable=False),
                    Column('password', String(50), nullable=False)
                    )


def downgrade():
    op.drop_table('useradmin')
