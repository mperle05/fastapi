"""last few coloumns to post table

Revision ID: 313a07664d5f
Revises: 8b7335e00c03
Create Date: 2023-05-28 23:04:12.841979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313a07664d5f'
down_revision = '8b7335e00c03'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass