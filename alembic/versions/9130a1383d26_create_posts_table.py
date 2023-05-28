"""create posts table

Revision ID: 01b2584928a5
Revises: 
Create Date: 2023-05-28 22:54:26.013153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
#revision = '01b2584928a5'
revision = 'c47ecbf163d4'
down_revision = None
branch_labels = None
depends_on = None




def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass