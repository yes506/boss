"""empty message

Revision ID: 296009a5ddcc
Revises: 
Create Date: 2022-01-13 07:26:34.161068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '296009a5ddcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('shop', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('shop_name', sa.String(length=200), nullable=True),
    sa.Column('shop_address', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop')
    op.drop_table('order')
    # ### end Alembic commands ###