"""empty message

Revision ID: a872583713eb
Revises: 
Create Date: 2021-04-16 13:45:23.895784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a872583713eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    op.drop_column('words', 'learned')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('words', sa.Column('learned', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###