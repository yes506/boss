"""empty message

Revision ID: 64cbd0f556b6
Revises: 296009a5ddcc
Create Date: 2022-01-17 06:47:22.067708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64cbd0f556b6'
down_revision = '296009a5ddcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calc',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('shop', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('order', sa.Column('price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'price')
    op.drop_table('calc')
    # ### end Alembic commands ###