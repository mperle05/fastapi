"""add content coloumn

Revision ID: add4fd927958
Revises: 01b2584928a5
Create Date: 2023-05-28 22:56:32.019635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add4fd927958'
down_revision = '01b2584928a5'

branch_labels = None
depends_on = None




def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass