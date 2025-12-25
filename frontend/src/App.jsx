import React, { useState } from 'react';
import { Search, ShieldAlert, Activity, Lock, ArrowRight, Zap } from 'lucide-react';
import { motion } from 'framer-motion';

function App() {
    const [identifier, setIdentifier] = useState('');
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!identifier) return;

        setLoading(true);
        try {
            const res = await fetch('/api/v1/exposure/check', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ value: identifier, type: 'email' })
            });
            const data = await res.json();
            setResult(data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="app-container">
            {/* Navbar */}
            <nav className="glass" style={{ padding: '20px 0', borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                <div className="container" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <Activity className="text-gradient" size={24} />
                        <h1 style={{ fontSize: '1.2rem', fontWeight: 700, letterSpacing: '1px' }}>TOTAL ENTITY</h1>
                    </div>
                    <div style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>Identity Risk Intelligence System</div>
                </div>
            </nav>

            {/* Hero / Input */}
            <section style={{ padding: '80px 0', textAlign: 'center' }}>
                <div className="container">
                    <motion.h1
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="text-gradient"
                        style={{ fontSize: '3.5rem', marginBottom: '20px', lineHeight: 1.1 }}
                    >
                        Don't just check for breaches.<br />know your blast radius.
                    </motion.h1>
                    <motion.p
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.1 }}
                        style={{ color: 'var(--text-muted)', fontSize: '1.2rem', maxWidth: '600px', margin: '0 auto 40px' }}
                    >
                        Stop asking "Was I breached?" Start asking "What do I fix first?"
                        TOTAL ENTITY calculates your exposure risk, identity graph, and remediation priority.
                    </motion.p>

                    <motion.form
                        initial={{ opacity: 0, scale: 0.95 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: 0.2 }}
                        onSubmit={handleSubmit}
                        className="glass"
                        style={{
                            maxWidth: '500px',
                            margin: '0 auto',
                            padding: '8px',
                            display: 'flex',
                            borderRadius: '50px',
                            border: '1px solid rgba(255,255,255,0.1)'
                        }}
                    >
                        <input
                            type="text"
                            placeholder="Enter email, phone, or username..."
                            value={identifier}
                            onChange={(e) => setIdentifier(e.target.value)}
                            style={{
                                flex: 1,
                                background: 'transparent',
                                border: 'none',
                                padding: '0 20px',
                                color: 'white',
                                outline: 'none',
                                fontSize: '1rem'
                            }}
                        />
                        <button type="submit" className="btn-primary" style={{ borderRadius: '40px', padding: '12px 30px' }}>
                            {loading ? 'Scanning...' : 'Analyze Risk'}
                        </button>
                    </motion.form>
                </div>
            </section>

            {/* Results */}
            {result && (
                <section style={{ padding: '0 0 80px' }}>
                    <div className="container">
                        {/* Score Cards */}
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', marginBottom: '40px' }}>
                            <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="card">
                                <div style={{ color: 'var(--text-muted)', marginBottom: '10px' }}>Risk Score</div>
                                <div style={{ fontSize: '3rem', fontWeight: 700, color: result.risk_score > 50 ? 'var(--danger)' : 'var(--success)' }}>
                                    {Math.round(result.risk_score)}<span style={{ fontSize: '1rem', color: 'var(--text-muted)' }}>/100</span>
                                </div>
                            </motion.div>
                            <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }} className="card">
                                <div style={{ color: 'var(--text-muted)', marginBottom: '10px' }}>Identified Breaches</div>
                                <div style={{ fontSize: '3rem', fontWeight: 700 }}>{result.breach_count}</div>
                            </motion.div>
                            <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2 }} className="card">
                                <div style={{ color: 'var(--text-muted)', marginBottom: '10px' }}>Exposed Services</div>
                                <div style={{ fontSize: '3rem', fontWeight: 700 }}>{result.graph.nodes.length - 1}</div>
                            </motion.div>
                        </div>

                        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '30px' }}>

                            {/* Action Plan */}
                            <div className="card">
                                <h2 style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '20px' }}>
                                    <Zap color="var(--warning)" /> Action Prioritization
                                </h2>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                                    {result.actions.map((action, idx) => (
                                        <div key={idx} style={{
                                            display: 'flex',
                                            justifyContent: 'space-between',
                                            alignItems: 'center',
                                            padding: '15px',
                                            background: 'rgba(255,255,255,0.03)',
                                            borderRadius: '8px',
                                            borderLeft: idx === 0 ? '4px solid var(--primary)' : '4px solid transparent'
                                        }}>
                                            <div>
                                                <div style={{ fontWeight: 600, fontSize: '1.1rem' }}>
                                                    {idx + 1}. {action.action.replace('_', ' ').toUpperCase()} on {action.service}
                                                </div>
                                                <div style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '5px' }}>
                                                    {action.reason}
                                                </div>
                                            </div>
                                            <div style={{ textAlign: 'right' }}>
                                                <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Priority</div>
                                                <div style={{ fontWeight: 700, color: 'var(--primary)' }}>{action.priority_score}</div>
                                            </div>
                                        </div>
                                    ))}
                                    {result.actions.length === 0 && <p style={{ color: 'var(--text-muted)' }}>No immediate actions required.</p>}
                                </div>
                            </div>

                            {/* Blast Radius / Identity Graph Simple View */}
                            <div className="card">
                                <h2 style={{ marginBottom: '20px' }}>Blast Radius</h2>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                                    {result.graph.nodes.map(node => (
                                        <div key={node.id} style={{
                                            padding: '10px',
                                            background: node.id === 'root' ? 'var(--primary)' : 'rgba(255,255,255,0.05)',
                                            borderRadius: '6px',
                                            fontSize: '0.9rem',
                                            display: 'flex',
                                            alignItems: 'center',
                                            gap: '10px'
                                        }}>
                                            <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'white' }}></div>
                                            {node.label} <span style={{ opacity: 0.5, fontSize: '0.8rem' }}>({node.type})</span>
                                        </div>
                                    ))}
                                </div>
                            </div>

                        </div>
                    </div>
                </section>
            )}
        </div>
    )
}

export default App
