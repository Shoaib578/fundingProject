"""empty message

Revision ID: 29889d8caa86
Revises: 35a9f0be651d
Create Date: 2023-06-19 16:31:05.108257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29889d8caa86'
down_revision = '35a9f0be651d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('due_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=30),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('due_date',
               existing_type=sa.String(length=30),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
