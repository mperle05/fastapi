"""create posts table

Revision ID: b47d2b4a7661
Revises: 
Create Date: 2023-05-27 22:20:49.775615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b47d2b4a7661'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
