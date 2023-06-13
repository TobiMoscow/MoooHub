"""Remove vedio column

Revision ID: 12be8a042851
Revises: e835317802c9
Create Date: 2023-05-28 11:37:15.784641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12be8a042851'
down_revision = 'e835317802c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('innovations', schema=None) as batch_op:
        batch_op.drop_column('video_link')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('innovations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('video_link', sa.VARCHAR(length=60), autoincrement=False, nullable=False))

    # ### end Alembic commands ###