"""empty message

Revision ID: 471e4dfb4b68
Revises: 
Create Date: 2021-10-20 08:40:42.254715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '471e4dfb4b68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient', sa.String(length=64), nullable=False),
    sa.Column('subject', sa.String(length=64), nullable=False),
    sa.Column('body', sa.String(length=255), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_emails_subject'), 'emails', ['subject'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_emails_subject'), table_name='emails')
    op.drop_table('emails')
    # ### end Alembic commands ###