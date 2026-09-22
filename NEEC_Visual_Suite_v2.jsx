import React, { useState } from 'react';
import { BarChart, Bar, RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis, 
         ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend, 
         ResponsiveContainer, Cell } from 'recharts';
import { Download, ChevronRight, Info } from 'lucide-react';

const NEECVisualSuite = () => {
  const [activeView, setActiveView] = useState('hierarchy');
  const [selectedSystem, setSelectedSystem] = useState('CCO-PTF-CIP-SZH');

  // Color palette
  const colors = {
    primary: '#2563eb',
    success: '#10b981',
    warning: '#f59e0b',
    danger: '#ef4444',
    neutral: '#6b7280',
    accent: '#8b5cf6'
  };

  // System performance data - CORRECTED from report
  // Domain 1 (Material Security) is out of 6; Domains 2-5 are each out of 5; Total is out of 26.
  // Source: canonical neec_scores.csv / neec_weighting_robustness_analysis_v2.py, all 15 systems,
  // cross-validated against NEEC Report v1.6 and NEEC Paper v1.3, September 2026.
  const systemScores = [
    { name: 'CCO-PTF-CIP-SZH', total: 24.5, domain1: 5.5, domain2: 5.0, domain3: 5.0, domain4: 4.5, domain5: 4.5, failures: 0, status: 'Potentially Adequate' },
    { name: 'Participatory Econ', total: 20.5, domain1: 5.0, domain2: 4.0, domain3: 4.5, domain4: 4.0, domain5: 3.0, failures: 1, status: 'Potentially Adequate' },
    { name: 'Nordic Social Dem', total: 19.5, domain1: 5.0, domain2: 3.5, domain3: 3.5, domain4: 3.5, domain5: 4.0, failures: 2, status: 'Potentially Adequate' },
    { name: 'Integral', total: 19.5, domain1: 3.0, domain2: 4.5, domain3: 5.0, domain4: 4.5, domain5: 2.5, failures: 3, status: 'Partially Adequate' },
    { name: 'Degrowth', total: 19.0, domain1: 4.5, domain2: 3.5, domain3: 4.0, domain4: 5.0, domain5: 2.0, failures: 2, status: 'Potentially Adequate' },
    { name: 'Market Socialism', total: 16.5, domain1: 4.0, domain2: 3.5, domain3: 3.0, domain4: 3.0, domain5: 3.0, failures: 2, status: 'Potentially Adequate' },
    { name: 'MMT + Job Guarantee', total: 15.5, domain1: 3.5, domain2: 2.5, domain3: 3.0, domain4: 3.5, domain5: 3.0, failures: 3, status: 'Partially Adequate' },
    { name: 'Mutual Credit/LETS', total: 14.5, domain1: 2.0, domain2: 3.0, domain3: 3.0, domain4: 2.5, domain5: 4.0, failures: 3, status: 'Partially Adequate' },
    { name: 'UBI', total: 14.5, domain1: 2.5, domain2: 3.0, domain3: 3.0, domain4: 3.0, domain5: 3.0, failures: 7, status: 'Structurally Inadequate' },
    { name: 'Georgism/LVT', total: 13.5, domain1: 2.0, domain2: 3.0, domain3: 3.0, domain4: 2.5, domain5: 3.0, failures: 2, status: 'Potentially Adequate' },
    { name: 'FALC', total: 13.0, domain1: 3.0, domain2: 3.0, domain3: 3.0, domain4: 3.5, domain5: 0.5, failures: 10, status: 'Structurally Inadequate' },
    { name: 'Status Quo Cap', total: 10.5, domain1: 2.0, domain2: 2.0, domain3: 2.0, domain4: 0.5, domain5: 4.0, failures: 9, status: 'Structurally Inadequate' },
    { name: 'Stakeholder Cap', total: 10.0, domain1: 2.0, domain2: 2.0, domain3: 2.5, domain4: 1.0, domain5: 2.5, failures: 9, status: 'Structurally Inadequate' },
    { name: 'Central Planning', total: 10.0, domain1: 3.0, domain2: 0.5, domain3: 2.5, domain4: 3.0, domain5: 1.0, failures: 12, status: 'Structurally Inadequate' },
    { name: 'Libertarian Min', total: 8.0, domain1: 0.0, domain2: 3.0, domain3: 0.5, domain4: 1.5, domain5: 3.0, failures: 15, status: 'Structurally Inadequate' },
  ];

  // Radar chart data for domains
  const getRadarData = (systemName) => {
    const system = systemScores.find(s => s.name === systemName);
    if (!system) return [];
    
    // Normalized to % of each domain's own max, since Domain 1 (Material Security) is out of 6
    // while Domains 2-5 are each out of 5 -- a shared raw fullMark would misrepresent Domain 1.
    return [
      { domain: 'Material Security', value: Math.round(system.domain1 / 6 * 100), fullMark: 100 },
      { domain: 'Human Autonomy', value: Math.round(system.domain2 / 5 * 100), fullMark: 100 },
      { domain: 'System Resilience', value: Math.round(system.domain3 / 5 * 100), fullMark: 100 },
      { domain: 'Ethical Integrity', value: Math.round(system.domain4 / 5 * 100), fullMark: 100 },
      { domain: 'Implementation', value: Math.round(system.domain5 / 5 * 100), fullMark: 100 },
    ];
  };

  // Pareto frontier data
  const paretoData = systemScores.map(sys => ({
    name: sys.name,
    resilience: sys.domain3,
    security: sys.domain1,
    total: sys.total,
    status: sys.status
  }));

  // Hierarchy visualization data
  const hierarchySteps = [
    { level: 1, title: '6 Empirical Premises', description: 'Observable features of contemporary reality', color: colors.danger },
    { level: 2, title: 'Derivation Logic', description: 'Philosophical reasoning from premises', color: colors.neutral },
    { level: 3, title: '14 Core Criteria', description: 'Conceptual evaluation standards', color: colors.warning },
    { level: 4, title: 'Operationalization', description: 'Converting concepts to measurements', color: colors.neutral },
    { level: 5, title: '26 Applied Criteria', description: 'Measurable evaluation metrics', color: colors.primary },
    { level: 6, title: '5 Domains', description: 'Organized evaluation framework', color: colors.success },
  ];

  const getStatusColor = (status) => {
    if (status === 'Potentially Adequate') return colors.success;
    if (status === 'Partially Adequate') return colors.warning;
    return colors.danger;
  };

  const renderHierarchy = () => (
    <div className="space-y-8">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">NEEC Hierarchical Structure</h2>
        <p className="text-gray-600">From empirical observation to operational measurement</p>
      </div>
      
      <div className="flex flex-col items-center space-y-6">
        {hierarchySteps.map((step, idx) => (
          <React.Fragment key={step.level}>
            <div 
              className="w-full max-w-2xl rounded-lg p-6 shadow-lg transition-all hover:shadow-xl"
              style={{ backgroundColor: step.color + '15', borderLeft: `4px solid ${step.color}` }}
            >
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="text-xl font-bold text-gray-900">{step.title}</h3>
                  <p className="text-gray-600 mt-1">{step.description}</p>
                </div>
                <div 
                  className="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-lg"
                  style={{ backgroundColor: step.color }}
                >
                  {step.level}
                </div>
              </div>
            </div>
            {idx < hierarchySteps.length - 1 && (
              <ChevronRight className="rotate-90 text-gray-400" size={32} />
            )}
          </React.Fragment>
        ))}
      </div>

      <div className="mt-12 grid grid-cols-5 gap-4 max-w-4xl mx-auto">
        <div className="col-span-5 text-center mb-4">
          <h3 className="text-xl font-bold text-gray-900">The 5 Evaluation Domains (26 Total Criteria)</h3>
        </div>
        {['Material Security', 'Human Autonomy', 'System Resilience', 'Ethical Integrity', 'Implementation'].map((domain, idx) => (
          <div key={domain} className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-blue-600 mb-2">{idx + 1}</div>
            <div className="text-sm font-medium text-gray-700">{domain}</div>
            <div className="text-xs text-gray-500 mt-1">{domain === 'Material Security' ? 6 : 5} criteria</div>
          </div>
        ))}
      </div>

      <div className="mt-16 max-w-6xl mx-auto">
        <div className="grid md:grid-cols-2 gap-8">
          {/* 14 Core Criteria */}
          <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl p-8 shadow-lg">
            <div className="text-center mb-6">
              <div className="text-6xl font-bold text-purple-600 mb-4">14</div>
              <h4 className="text-2xl font-bold text-gray-900 mb-3">Core Criteria</h4>
              <p className="text-gray-700 text-sm leading-relaxed mb-4">
                Philosophically explicit principles derived from six empirical premises.
              </p>
            </div>
            <div className="space-y-2 text-sm">
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N1.</span> Human Flourishing Primacy</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N2.</span> Labor Non-Necessity</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N3.</span> Coercion Minimization</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N4.</span> Universal Wealth Access</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N5.</span> Crisis and Shock Robustness</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N6.</span> Ecological Compliance</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N7.</span> Governance Legitimacy & Anti-Capture</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N8.</span> Epistemic Adaptability</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N9.</span> Partial and Parallel Deployability</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N10.</span> Failure-Mode Transparency</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N11.</span> Automation Compatibility</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N12.</span> Intergenerational Equity</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N13.</span> Incentive Alignment (Micro ↔ Macro)</div>
              <div className="bg-white bg-opacity-60 rounded p-2"><span className="font-semibold">N14.</span> Global Scalability Without Extraction</div>
            </div>
          </div>

          {/* 25 Applied Criteria */}
          <div className="bg-gradient-to-br from-indigo-50 to-indigo-100 rounded-xl p-8 shadow-lg">
            <div className="text-center mb-6">
              <div className="text-6xl font-bold text-indigo-600 mb-4">26</div>
              <h4 className="text-2xl font-bold text-gray-900 mb-3">Applied Criteria</h4>
              <p className="text-gray-700 text-sm leading-relaxed mb-4">
                Operationalized metrics with empirical thresholds across five domains.
              </p>
            </div>
            <div className="space-y-3 text-sm">
              <div>
                <div className="font-bold text-indigo-800 mb-1">Domain 1: Material Security</div>
                <div className="space-y-1 ml-3">
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C1.1 Poverty Elimination</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C1.2a Wealth Building for Resilience</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C1.2b Prevention of Exploitative Accumulation</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C1.3 Housing Security</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C1.4 Automation Resilience</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C1.5 Universal Wealth Access</div>
                </div>
              </div>
              <div>
                <div className="font-bold text-indigo-800 mb-1">Domain 2: Human Autonomy</div>
                <div className="space-y-1 ml-3">
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C2.1 Freedom from Coercion</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C2.2 Labor Non-Necessity</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C2.3 Creative Development</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C2.4 Democratic Participation</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C2.5 Exit Rights & Mobility</div>
                </div>
              </div>
              <div>
                <div className="font-bold text-indigo-800 mb-1">Domain 3: System Resilience</div>
                <div className="space-y-1 ml-3">
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C3.1 Crisis Response</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C3.2 Inflation Control</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C3.3 Multi-Failure Resistance</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C3.4 Epistemic Adaptability</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C3.5 Failure-Mode Transparency</div>
                </div>
              </div>
              <div>
                <div className="font-bold text-indigo-800 mb-1">Domain 4: Ethical Integrity</div>
                <div className="space-y-1 ml-3">
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C4.1 Intergenerational Justice</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C4.2 Ecological Compliance</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C4.3 Racial & Gender Equity</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C4.4 Power Distribution</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C4.5 Exploitation Elimination</div>
                </div>
              </div>
              <div>
                <div className="font-bold text-indigo-800 mb-1">Domain 5: Implementation</div>
                <div className="space-y-1 ml-3">
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C5.1 Proven Components</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C5.2 Staged Transition</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C5.3 Partial Deployability</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C5.4 Political Coalition</div>
                  <div className="bg-white bg-opacity-60 rounded p-1.5">C5.5 Cultural Adaptability</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const renderComparison = () => (
    <div className="space-y-8">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">System Performance Comparison</h2>
        <p className="text-gray-600">Total scores across all 26 criteria (max: 26)</p>
      </div>

      <ResponsiveContainer width="100%" height={500}>
        <BarChart data={systemScores} layout="vertical" margin={{ left: 150, right: 30 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" domain={[0, 26]} />
          <YAxis type="category" dataKey="name" width={140} />
          <Tooltip 
            content={({ active, payload }) => {
              if (active && payload && payload[0]) {
                const data = payload[0].payload;
                return (
                  <div className="bg-white p-4 rounded-lg shadow-lg border">
                    <p className="font-bold text-gray-900">{data.name}</p>
                    <p className="text-gray-700">Total Score: {data.total}/26 ({(data.total/26*100).toFixed(0)}%)</p>
                    <p className="text-gray-700">Structural Failures: {data.failures}</p>
                    <p className="text-sm mt-2" style={{ color: getStatusColor(data.status) }}>
                      {data.status}
                    </p>
                  </div>
                );
              }
              return null;
            }}
          />
          <Bar dataKey="total" radius={[0, 8, 8, 0]}>
            {systemScores.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={getStatusColor(entry.status)} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>

      <div className="grid grid-cols-3 gap-4 max-w-3xl mx-auto mt-8">
        <div className="bg-green-50 border-l-4 border-green-500 rounded-lg p-4">
          <div className="text-sm font-medium text-gray-600">Potentially Adequate</div>
          <div className="text-2xl font-bold text-green-600">6 systems</div>
          <div className="text-xs text-gray-500 mt-1">&lt;3 structural failures</div>
        </div>
        <div className="bg-yellow-50 border-l-4 border-yellow-500 rounded-lg p-4">
          <div className="text-sm font-medium text-gray-600">Partially Adequate</div>
          <div className="text-2xl font-bold text-yellow-600">3 systems</div>
          <div className="text-xs text-gray-500 mt-1">3-5 structural failures</div>
        </div>
        <div className="bg-red-50 border-l-4 border-red-500 rounded-lg p-4">
          <div className="text-sm font-medium text-gray-600">Structurally Inadequate</div>
          <div className="text-2xl font-bold text-red-600">6 systems</div>
          <div className="text-xs text-gray-500 mt-1">&ge;6 structural failures</div>
        </div>
      </div>
    </div>
  );

  const renderRadar = () => {
    const system = systemScores.find(s => s.name === selectedSystem);
    
    return (
      <div className="space-y-8">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-2">Domain-Level Analysis</h2>
          <p className="text-gray-600">Performance across five evaluation domains</p>
        </div>

        <div className="flex justify-center mb-8 flex-wrap gap-2">
          <div className="inline-flex rounded-lg border border-gray-300 p-1 flex-wrap">
            {systemScores.map(sys => (
              <button
                key={sys.name}
                onClick={() => setSelectedSystem(sys.name)}
                className={`px-3 py-2 rounded-md transition-colors text-sm ${
                  selectedSystem === sys.name
                    ? 'bg-blue-600 text-white'
                    : 'text-gray-700 hover:bg-gray-100'
                }`}
              >
                {sys.name}
              </button>
            ))}
          </div>
        </div>

        <ResponsiveContainer width="100%" height={500}>
          <RadarChart data={getRadarData(selectedSystem)}>
            <PolarGrid stroke="#e5e7eb" />
            <PolarAngleAxis dataKey="domain" tick={{ fill: '#374151', fontSize: 12 }} />
            <PolarRadiusAxis angle={90} domain={[0, 100]} tick={{ fill: '#6b7280' }} />
            <Radar
              name={selectedSystem}
              dataKey="value"
              stroke={colors.primary}
              fill={colors.primary}
              fillOpacity={0.3}
            />
            <Tooltip 
              content={({ active, payload }) => {
                if (active && payload && payload[0]) {
                  return (
                    <div className="bg-white p-3 rounded-lg shadow-lg border">
                      <p className="font-bold text-gray-900">{payload[0].payload.domain}</p>
                      <p className="text-gray-700">Score: {payload[0].value}% of this domain's max</p>
                    </div>
                  );
                }
                return null;
              }}
            />
          </RadarChart>
        </ResponsiveContainer>

        {system && (
          <div className="max-w-2xl mx-auto mt-8">
            <div className="bg-gray-50 rounded-lg p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4">{selectedSystem} Summary</h3>
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span className="text-gray-600">Total Score:</span>
                  <span className="font-bold">{system.total}/26 ({(system.total/26*100).toFixed(0)}%)</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Structural Failures:</span>
                  <span className="font-bold">{system.failures}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Status:</span>
                  <span className="font-bold" style={{ color: getStatusColor(system.status) }}>
                    {system.status}
                  </span>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    );
  };

  const renderPareto = () => (
    <div className="space-y-8">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Pareto Frontier Analysis</h2>
        <p className="text-gray-600">Total Score vs. Material Security (Domain 1, out of 6)</p>
        <p className="text-sm text-gray-500 mt-2 max-w-3xl mx-auto">
          The Pareto frontier identifies non-dominated systems—those where no alternative performs 
          strictly better across all measured dimensions. Systems below the frontier are dominated, 
          meaning superior alternatives exist.
        </p>
      </div>

      <ResponsiveContainer width="100%" height={500}>
        <ScatterChart margin={{ top: 20, right: 30, bottom: 60, left: 60 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            type="number" 
            dataKey="total" 
            name="Total Score"
            domain={[0, 27]}
            label={{ value: 'Total NEEC Score (Maximum: 26)', position: 'bottom', offset: 40 }}
          />
          <YAxis 
            type="number" 
            dataKey="security" 
            name="Material Security"
            domain={[0, 6]}
            label={{ value: 'Material Security Score (Maximum: 6)', angle: -90, position: 'left', offset: 40 }}
          />
          <Tooltip 
            content={({ active, payload }) => {
              if (active && payload && payload[0]) {
                const data = payload[0].payload;
                return (
                  <div className="bg-white p-4 rounded-lg shadow-lg border">
                    <p className="font-bold text-gray-900">{data.name}</p>
                    <p className="text-gray-700">Total Score: {data.total}/26</p>
                    <p className="text-gray-700">Material Security: {data.security}/6</p>
                    <p className="text-gray-700">System Resilience: {data.resilience}/5</p>
                    <p className="text-sm mt-2" style={{ color: getStatusColor(data.status) }}>
                      {data.status}
                    </p>
                  </div>
                );
              }
              return null;
            }}
          />
          <Scatter data={paretoData} fill="#8884d8">
            {paretoData.map((entry, index) => {
              const isParetoFrontier = ['CCO-PTF-CIP-SZH', 'Nordic Social Dem', 'Degrowth', 'Participatory Econ', 'Mutual Credit/LETS', 'Integral'].includes(entry.name);
              const size = isParetoFrontier ? 12 : 8;
              return (
                <Cell 
                  key={`cell-${index}`} 
                  fill={getStatusColor(entry.status)}
                  stroke={isParetoFrontier ? '#1f2937' : 'transparent'}
                  strokeWidth={isParetoFrontier ? 3 : 0}
                  r={size}
                />
              );
            })}
          </Scatter>
        </ScatterChart>
      </ResponsiveContainer>

      <div className="max-w-3xl mx-auto bg-blue-50 border-l-4 border-blue-500 rounded-lg p-6">
        <div className="flex items-start">
          <Info className="text-blue-600 mt-1 mr-3 flex-shrink-0" size={24} />
          <div>
            <h3 className="font-bold text-gray-900 mb-2">Understanding the Pareto Frontier</h3>
            <p className="text-gray-700 text-sm mb-3">
              Six systems lie on the Pareto frontier restricted to systems that clear NEEC's
              own adequacy bar (bold circles with black borders): CCO-PTF-CIP-SZH, Nordic Social
              Democracy, Degrowth Economics, Participatory Economics, Mutual Credit/LETS, and
              Integral. Each is non-dominated within that adequate-tier subset — no other adequate
              system outperforms it across every one of NEEC's 26 criteria simultaneously.
            </p>
            <p className="text-gray-700 text-sm mb-3">
              Market Socialism, Georgism/LVT, and MMT + Job Guarantee, though themselves adequate,
              are each strictly dominated by CCO-PTF-CIP-SZH specifically and are excluded from
              this narrower cut.
            </p>
            <p className="text-gray-700 text-sm">
              Across the <span className="font-semibold">full</span> 15-system corpus (not shown
              with bold markers here, to keep the chart legible), the unrestricted Pareto frontier
              is actually larger — 10 of 15 systems, including several Structurally Inadequate ones
              that escape formal dominance through a single narrow criterion (usually C4.5,
              Exploitation Elimination). Formal non-domination is not the same as merit; the
              six-system, adequate-tier-restricted frontier above is the practically useful cut.
              See the companion Report (Part II, Pareto Frontier Analysis) for the full account.
            </p>
          </div>
        </div>
      </div>
    </div>
  );

  const renderKeyInsights = () => (
    <div className="space-y-8">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Key Insights</h2>
        <p className="text-gray-600">Critical findings from NEEC evaluation</p>
      </div>

      <div className="grid md:grid-cols-2 gap-6 max-w-5xl mx-auto">
        <div className="bg-gradient-to-br from-red-50 to-red-100 rounded-lg p-6 shadow-lg">
          <h3 className="text-xl font-bold text-red-800 mb-3">Most Discriminating Criteria</h3>
          <div className="text-4xl font-bold text-red-600 mb-3">C1.2a / C1.5</div>
          <p className="text-gray-700 font-medium mb-2">Wealth Building &amp; Access</p>
          <p className="text-gray-600 text-sm">
            Each fails 7 of 15 systems outright -- more than automation resilience or ecological
            compliance (3 each). Splitting the legacy wealth criterion into resilience-building
            and concentration-prevention halves revealed this, since a system's strength on one
            half used to mask its weakness on the other.
          </p>
        </div>

        <div className="bg-gradient-to-br from-yellow-50 to-yellow-100 rounded-lg p-6 shadow-lg">
          <h3 className="text-xl font-bold text-yellow-800 mb-3">Best Existing System</h3>
          <div className="text-4xl font-bold text-yellow-600 mb-3">75%</div>
          <p className="text-gray-700 font-medium mb-2">Nordic Social Democracy</p>
          <p className="text-gray-600 text-sm">
            Highest score among implemented systems (19.5/26), achieving potentially adequate
            status with only 2 structural failures. Exactly tied on percentage with Integral (also
            75%), which reaches the same score through an unproven design with a third failure.
          </p>
        </div>

        <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-lg p-6 shadow-lg">
          <h3 className="text-xl font-bold text-blue-800 mb-3">A Real Middle Tier</h3>
          <div className="text-4xl font-bold text-blue-600 mb-3">3</div>
          <p className="text-gray-700 font-medium mb-2">Systems in 3-5 Failure Range</p>
          <p className="text-gray-600 text-sm">
            Integral, MMT + Job Guarantee, and Mutual Credit/LETS each land in a genuine, structurally
            distinct Partially Adequate tier -- reached through three entirely different underlying
            designs, not an artifact of an incomplete scale.
          </p>
        </div>

        <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-lg p-6 shadow-lg">
          <h3 className="text-xl font-bold text-green-800 mb-3">Viable Alternatives</h3>
          <div className="text-4xl font-bold text-green-600 mb-3">9/15</div>
          <p className="text-gray-700 font-medium mb-2">Potentially or Partially Adequate</p>
          <p className="text-gray-600 text-sm">
            Six systems clear the full adequacy bar and three more come close enough to be a concrete
            reform target, demonstrating transformation is feasible through diverse pathways: existing
            proven, cooperative, macroeconomic, ecological, fiscal, and comprehensive integrated.
          </p>
        </div>
      </div>

      <div className="max-w-4xl mx-auto mt-12 bg-gray-900 text-white rounded-lg p-8">
        <h3 className="text-2xl font-bold mb-4">The Choice Before Humanity</h3>
        <p className="text-gray-300 mb-4">
          Six systems demonstrate full adequacy, and three more come close enough to be a concrete
          reform target rather than a rejected alternative. The evidence is clear: superior
          alternatives exist with proven components and actionable pathways.
        </p>
        <div className="flex items-center text-blue-400 font-medium">
          <span>NEEC provides the standard. The frameworks are specified. The choice belongs to democratic publics.</span>
        </div>
        <p className="text-gray-400 text-sm mt-4 italic">
          What remains is political will and democratic courage.
        </p>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            NEEC Visual Suite
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Interactive visualizations of the Normative Economic Evaluation Criteria framework
          </p>
          <div className="mt-6 flex justify-center space-x-4">
            <a 
              href="https://sites.google.com/view/normativeeconomicevaluation/paper" 
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-700 underline"
            >
              Read the full paper →
            </a>
            <span className="text-gray-400">|</span>
            <a 
              href="https://sites.google.com/view/normativeeconomicevaluation/report" 
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-700 underline"
            >
              View detailed report →
            </a>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex justify-center mb-12">
          <div className="inline-flex rounded-lg border border-gray-300 bg-white p-1 shadow-sm">
            {[
              { id: 'hierarchy', label: 'Framework Structure' },
              { id: 'comparison', label: 'System Comparison' },
              { id: 'radar', label: 'Domain Analysis' },
              { id: 'pareto', label: 'Pareto Frontier' },
              { id: 'insights', label: 'Key Insights' }
            ].map(view => (
              <button
                key={view.id}
                onClick={() => setActiveView(view.id)}
                className={`px-6 py-3 rounded-md transition-all font-medium ${
                  activeView === view.id
                    ? 'bg-blue-600 text-white shadow-md'
                    : 'text-gray-700 hover:bg-gray-100'
                }`}
              >
                {view.label}
              </button>
            ))}
          </div>
        </div>

        {/* Content */}
        <div className="bg-white rounded-xl shadow-xl p-8 mb-8">
          {activeView === 'hierarchy' && renderHierarchy()}
          {activeView === 'comparison' && renderComparison()}
          {activeView === 'radar' && renderRadar()}
          {activeView === 'pareto' && renderPareto()}
          {activeView === 'insights' && renderKeyInsights()}
        </div>

        {/* Footer */}
        <div className="text-center text-gray-600 text-sm">
          <p>NEEC: Normative Economic Evaluation Criteria</p>
          <p className="mt-2">
            <a 
              href="https://IndependentResearcher.academia.edu/DukeJohnson"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-700 underline"
            >
              Johnson, D.
            </a>
            {' '}& Claude (Anthropic). 2026.
          </p>
          <p className="mt-2">Licensed under CC BY 4.0</p>
        </div>
      </div>
    </div>
  );
};

export default NEECVisualSuite;