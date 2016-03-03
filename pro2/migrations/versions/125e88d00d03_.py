"""empty message

Revision ID: 125e88d00d03
Revises: 3dad725dafa3
Create Date: 2016-03-03 12:47:06.967010

"""

# revision identifiers, used by Alembic.
revision = '125e88d00d03'
down_revision = '3dad725dafa3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
